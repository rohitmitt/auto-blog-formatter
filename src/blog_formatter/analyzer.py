import spacy
from typing import Dict, Any

class TextAnalyzer:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
        
    def analyze_text(self, text: str) -> Dict[str, Any]:
        """Analyze text and extract structural components."""
        doc = self.nlp(text)
        
        # Split text into lines
        lines = text.split('\n')
        
        # Basic structure analysis
        structure = {
            'title': '',
            'subtitle': '',
            'body': [],
            'metadata': {}
        }
        
        # More sophisticated title detection
        for line in lines:
            line = line.strip()
            if line:
                # Title should be relatively short and not end with punctuation
                if len(line.split()) <= 8 and not line[-1] in '.!?':
                    structure['title'] = line
                    break
                else:
                    # If first line doesn't look like a title, treat everything as body
                    structure['body'].append(line)
                    return structure
                
        # Subtitle detection - should be longer than title but not a full paragraph
        subtitle_found = False
        for line in lines[1:]:
            line = line.strip()
            if line:
                if len(line.split()) <= 15 and not any(sent.endswith('.') for sent in line.split('. ')):
                    structure['subtitle'] = line
                    subtitle_found = True
                break
        
        # Process body paragraphs
        start_idx = 2 if subtitle_found else 1
        current_paragraph = []
        
        for line in lines[start_idx:]:
            if not line.strip():  # Empty line indicates paragraph break
                if current_paragraph:
                    structure['body'].append(' '.join(current_paragraph))
                    current_paragraph = []
            else:
                current_paragraph.append(line.strip())
        
        # Append last paragraph if exists
        if current_paragraph:
            structure['body'].append(' '.join(current_paragraph))
        
        # Analyze sentiment and key phrases
        structure['metadata']['sentiment'] = self._analyze_sentiment(doc)
        structure['metadata']['key_phrases'] = self._extract_key_phrases(doc)
        
        return structure
    
    def _analyze_sentiment(self, doc) -> str:
        """Basic sentiment analysis."""
        # Simple polarity scoring based on positive/negative words
        positive_words = sum(1 for token in doc if token.pos_ == 'ADJ' and token.is_stop == False)
        negative_words = sum(1 for token in doc if token.pos_ == 'ADV' and token.is_stop == False)
        return 'positive' if positive_words > negative_words else 'neutral'
    
    def _extract_key_phrases(self, doc) -> list:
        """Extract important phrases using noun chunks."""
        return [chunk.text for chunk in doc.noun_chunks][:10]  # Get top 5 phrases
