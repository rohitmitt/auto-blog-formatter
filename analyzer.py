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
        
        # Simple heuristic: first non-empty line is usually the title
        for line in lines:
            if line.strip():
                structure['title'] = line.strip()
                break
                
        # Look for potential subtitle (next non-empty line after title)
        subtitle_found = False
        for line in lines[1:]:
            if line.strip():
                structure['subtitle'] = line.strip()
                subtitle_found = True
                break
                
        # Rest is considered body
        start_idx = 2 if subtitle_found else 1
        structure['body'] = [line.strip() for line in lines[start_idx:] if line.strip()]
        
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
        return [chunk.text for chunk in doc.noun_chunks][:5]  # Get top 5 phrases
