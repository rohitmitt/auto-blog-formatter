import argparse
import sys
import json
from analyzer import TextAnalyzer

class BlogFormatter:
    def __init__(self, config_path=None):
        self.config = self.load_config(config_path)
        self.analyzer = TextAnalyzer()

    def load_config(self, config_path):
        if not config_path:
            return {}
        try:
            with open(config_path, 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading config: {e}")
            return {}

    def format_text(self, text):
        # Analyze the text structure
        analysis = self.analyzer.analyze_text(text)
        
        # Generate HTML with CSS classes
        html_output = f"""
        <article class="blog-post">
            <h1 class="title">{analysis['title']}</h1>
            {f'<h2 class="subtitle">{analysis["subtitle"]}</h2>' if analysis['subtitle'] else ''}
            {''.join(f'<p class="body-text">{para}</p>' for para in analysis['body'])}
        </article>
        """
        
        return html_output

def main():
    parser = argparse.ArgumentParser(description='Blog text formatter')
    parser.add_argument('--input', '-i', help='Input file path')
    parser.add_argument('--config', '-c', help='Configuration file path')
    
    args = parser.parse_args()
    
    formatter = BlogFormatter(args.config)
    
    if args.input:
        with open(args.input, 'r') as f:
            text = f.read()
    else:
        text = sys.stdin.read()
    
    formatted_text = formatter.format_text(text)
    print(formatted_text)

if __name__ == "__main__":
    main()
