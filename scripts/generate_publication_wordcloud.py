"""Render a deterministic word cloud from 2023+ publication titles and five research themes.

Requires wordcloud, numpy, and Pillow. Run from any directory with Python 3.
"""
from pathlib import Path
import os
import re
import numpy as np
from wordcloud import WordCloud

ROOT = Path(__file__).resolve().parents[1]
text = (ROOT / '_pages/publications.md').read_text()
recent = text.split('<a id="2022"', 1)[0]
titles = re.findall(r'^\*\*(.+?)\*\*', recent, re.M)
titles = [title for title in titles if not re.fullmatch(r'\d{4}', title)]
corpus = ' '.join(titles)
# Give each project a visible place, then weight topics using their title frequency.
frequencies = {'Cyber Threats': 100, 'Scams & Fraud': 94, 'Mobile Security': 98,
               'Smart Contracts': 92, 'Software Analysis': 96}
patterns = {
    'LLMs': r'LLM|Language Model', 'AI Agents': r'Agents?',
    'Provenance Graphs': r'Provenance', 'Attack Investigation': r'Investigation',
    'Privacy': r'Privacy|Private', 'Malware Detection': r'Malware',
    'Program Analysis': r'Analysis|Analyz', 'Vulnerability Repair': r'Vulnerabilit',
    'Threat Intelligence': r'Threat Intelligence', 'Symbolic Planning': r'Symbolic Planning',
    'Scam Progression': r'Scam Progression', 'Psychological Techniques': r'Psychological',
    'Augmented Reality': r'Android AR', 'Knowledge Graphs': r'Knowledge Graph',
    'Sensitive Behaviors': r'Sensitive Behavior', 'Static Analysis': r'Tainting|Behavior Analysis',
    'Graph Learning': r'Graph Model|Graph Reasoning|App Promotion Graph',
    'Counterfactuals': r'Counterfactual', 'App Ecosystems': r'App Promotion|Mini-Program',
    'Conformance Testing': r'Conformance', 'RISC-V': r'RISC-V',
    'UI Automation': r'UI Agent', 'Robustness': r'Uncertainty',
    'Smart Contract Synthesis': r'Contract Synthesis', 'User Awareness': r'User Privacy',
    'Explainability': r'Explain|Description Synthesis', 'Query Languages': r'Query',
    'PsyScam': r'PsyScam', 'PreScam': r'PreScam', 'ProGQL': r'ProGQL',
    'CTIKG': r'CTIKG', 'Agent+P': r'Agent\+P', 'vFix': r'vFix',
    'APT Detection': r'APT|DISTDET', 'Mini-Programs': r'Mini-Program',
}
for phrase, pattern in patterns.items():
    count = len(re.findall(pattern, corpus, re.I))
    if count:
        frequencies[phrase] = min(78, 24 + count * 7)
# Older foundational work remains represented through the research directions.
research = (ROOT / '_pages/research.md').read_text()
for phrase in ['Causality Analysis', 'Contextual Integrity', 'Software Testing',
               'Blockchain', 'Interoperability', 'Log Storage', 'Data Flow']:
    if phrase.lower() in research.lower() or phrase in ['Log Storage', 'Data Flow']:
        frequencies[phrase] = 34
font = os.environ.get('WORDCLOUD_FONT')
if not font:
    candidates = ['/System/Library/Fonts/Supplemental/Trebuchet MS Bold.ttf',
                  '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf']
    font = next((path for path in candidates if Path(path).exists()), None)
y, x = np.ogrid[:1000, :1800]
mask = np.where(((x-900)/880)**2 + ((y-500)/480)**2 > 1, 255, 0).astype(np.uint8)
colors = ['#8c1d40', '#216c78', '#32313d', '#aa7100', '#63507d']
def color(word, font_size, position, orientation, random_state=None, **kwargs):
    if word in ['Cyber Threats', 'Mobile Security', 'Software Analysis']:
        return '#8c1d40'
    if word in ['Scams & Fraud', 'Smart Contracts']:
        return '#216c78'
    return random_state.choice(colors)
cloud = WordCloud(width=1800, height=1000, scale=1.5, background_color='white',
                  mask=mask, font_path=font, max_words=55, max_font_size=108,
                  min_font_size=23, margin=9, prefer_horizontal=1,
                  relative_scaling=0.45, random_state=17, color_func=color,
                  collocations=False).generate_from_frequencies(frequencies)
themes = {'Cyber Threats', 'Scams & Fraud', 'Mobile Security', 'Smart Contracts', 'Software Analysis'}
assert themes <= {item[0][0] for item in cloud.layout_}, 'All five projects must appear.'
cloud.to_file(str(ROOT / 'images/publication-wordcloud.png'))
print(f'Rendered {len(cloud.layout_)} topics from {len(titles)} recent publications and five research directions.')
