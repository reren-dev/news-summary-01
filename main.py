# Copy summary.txt to MAKEFUN_OUTPUT_DIR/entry.txt, byte for byte.
import os
import sys

def main():
    summary_path = os.path.join(os.path.dirname(__file__), 'summary.txt')
    with open(summary_path, 'rb') as f:
        content = f.read()
    
    output_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, 'entry.txt')
    
    with open(output_path, 'wb') as f:
        f.write(content)

if __name__ == '__main__':
    main()
