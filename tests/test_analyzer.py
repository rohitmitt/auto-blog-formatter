import pytest
from src.blog_formatter.analyzer import TextAnalyzer

@pytest.fixture
def analyzer():
    return TextAnalyzer()

@pytest.fixture
def sample_text():
    return """The Future of Artificial Intelligence
A Journey into Tomorrow's Technology
    
AI is rapidly evolving and changing our world. The advancements in machine learning
have opened up new possibilities across various industries.

Healthcare and transportation are among the sectors seeing the biggest impact.
These changes are reshaping how we live and work."""

def test_basic_structure(analyzer, sample_text):
    result = analyzer.analyze_text(sample_text)
    assert 'title' in result
    assert 'subtitle' in result
    assert 'body' in result
    assert 'metadata' in result

def test_title_extraction(analyzer, sample_text):
    result = analyzer.analyze_text(sample_text)
    assert result['title'] == "The Future of Artificial Intelligence"
    assert result['subtitle'] == "A Journey into Tomorrow's Technology"

def test_body_extraction(analyzer, sample_text):
    result = analyzer.analyze_text(sample_text)
    assert len(result['body']) == 2
    assert "AI is rapidly evolving" in result['body'][0]

def test_metadata_structure(analyzer, sample_text):
    result = analyzer.analyze_text(sample_text)
    assert 'sentiment' in result['metadata']
    assert 'key_phrases' in result['metadata']
    assert isinstance(result['metadata']['key_phrases'], list)
    print("\nMetadata Analysis Results:")
    print(f"Sentiment: {result['metadata']['sentiment']}")
    print(f"Key Phrases: {', '.join(result['metadata']['key_phrases'])}")

def test_empty_text(analyzer):
    result = analyzer.analyze_text("")
    assert result['title'] == ""
    assert result['subtitle'] == ""
    assert len(result['body']) == 0
