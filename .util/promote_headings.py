import os
import re
import sys

def promote_headings(content):
    """
    Promotes headings in markdown content:
    ## -> #
    ### -> ##
    #### -> ###
    ##### -> ####
    ###### -> #####
    
    Note: It does NOT promote # to anything (stays # or could be handled if needed, 
    but usually # is the top level).
    """
    
    # We use a regex that matches headings at the start of a line.
    # We process from ## down to ###### to avoid double-promoting.
    # Actually, a single regex with a lambda replacement is safer to avoid 
    # ## becoming # and then # being ignored or processed again.
    
    def replace_heading(match):
        hashes = match.group(1)
        # Promote: ## -> #, ### -> ##, etc.
        # We don't promote # to nothing.
        return '#' * (len(hashes) - 1) + match.group(2)

    # Regex: start of line, 2-6 hashes, followed by space or end of line
    new_content = re.sub(r'^(#{2,6})(\s.*|$)', replace_heading, content, flags=re.MULTILINE)
    
    return new_content

def process_file(filepath, dry_run=True):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = promote_headings(content)
        
        if content != new_content:
            if dry_run:
                print(f"[DRY RUN] Would update: {filepath}")
            else:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated: {filepath}")
        else:
            print(f"No changes needed: {filepath}")
            
    except Exception as e:
        print(f"Error processing {filepath}: {e}")

def main():
    # Directories to search for summaries
    search_dirs = [
        'Admin Law/summaries', 
        'Copyright Law/05-summaries', 
        'Corporate Law/summaries'
    ]
    
    dry_run = '--apply' not in sys.argv
    
    if dry_run:
        print("Running in DRY RUN mode. Use --apply to actually modify files.\n")

    for s_dir in search_dirs:
        if not os.path.exists(s_dir):
            print(f"Directory not found: {s_dir}")
            continue
            
        for root, dirs, files in os.walk(s_dir):
            for file in files:
                if file.endswith('.md'):
                    filepath = os.path.join(root, file)
                    process_file(filepath, dry_run=dry_run)

if __name__ == "__main__":
    main()
