#!/usr/bin/env python3
"""
Compare Screen Studio JSON transcripts with corrected SRT files.
Focus on semantic differences, not styling or punctuation.
"""

import json
import re
from pathlib import Path
from difflib import SequenceMatcher
from typing import List, Dict, Tuple

# Define file pairs
MODULES = [
    {
        "name": "intro",
        "json": "/Users/matteolombardi/Screen Studio Projects/intro.screenstudio/recording/channel-2-microphone-0.m4a-transcript.json",
        "srt": "/Users/matteolombardi/AI-Projects/stratega/stratega-academy/school transcripts/intro-corrected.srt"
    },
    {
        "name": "m2-ICP",
        "json": "/Users/matteolombardi/Screen Studio Projects/mod2-ICP.screenstudio/recording/channel-2-microphone-0.m4a-transcript.json",
        "srt": "/Users/matteolombardi/AI-Projects/stratega/stratega-academy/school transcripts/m2-ICP-corrected.srt"
    },
    {
        "name": "m3-icp",
        "json": "/Users/matteolombardi/Screen Studio Projects/m3-icp.screenstudio/recording/channel-2-microphone-0.m4a-transcript.json",
        "srt": "/Users/matteolombardi/AI-Projects/stratega/stratega-academy/school transcripts/m3-icp-corrected.srt"
    },
    {
        "name": "m4-content",
        "json": "/Users/matteolombardi/Screen Studio Projects/m4-content.screenstudio/recording/channel-2-microphone-0.m4a-transcript.json",
        "srt": "/Users/matteolombardi/AI-Projects/stratega/stratega-academy/school transcripts/m4-content-corrected.srt"
    },
    {
        "name": "m5-copy",
        "json": "/Users/matteolombardi/Screen Studio Projects/m5-copy.screenstudio/recording/channel-2-microphone-0.m4a-transcript.json",
        "srt": "/Users/matteolombardi/AI-Projects/stratega/stratega-academy/school transcripts/m5-copy-corrected.srt"
    },
    {
        "name": "m6-tools",
        "json": "/Users/matteolombardi/Screen Studio Projects/m6-tools.screenstudio/recording/channel-2-microphone-0.m4a-transcript.json",
        "srt": "/Users/matteolombardi/AI-Projects/stratega/stratega-academy/school transcripts/m6-tools-corrected.srt"
    },
    {
        "name": "m7-ops",
        "json": "/Users/matteolombardi/Screen Studio Projects/m7-ops.screenstudio/recording/channel-2-microphone-0.m4a-transcript.json",
        "srt": "/Users/matteolombardi/AI-Projects/stratega/stratega-academy/school transcripts/m7-ops-corrected.srt"
    },
    {
        "name": "m8-fin",
        "json": "/Users/matteolombardi/Screen Studio Projects/m8-fin.screenstudio/recording/channel-2-microphone-0.m4a-transcript.json",
        "srt": "/Users/matteolombardi/AI-Projects/stratega/stratega-academy/school transcripts/m8-fin-corrected.srt"
    }
]

# Filler words to ignore
FILLERS = {'um', 'uh', 'like', 'you know', 'sort of', 'kind of', 'i mean', 'basically', 'actually', 'literally'}


def normalize_text(text: str) -> str:
    """Normalize text for comparison - remove punctuation, lowercase, remove extra spaces."""
    # Lowercase
    text = text.lower()
    # Remove punctuation but keep apostrophes in contractions
    text = re.sub(r"[^\w\s']", ' ', text)
    # Remove filler words
    for filler in FILLERS:
        text = re.sub(r'\b' + filler + r'\b', '', text, flags=re.IGNORECASE)
    # Normalize whitespace
    text = ' '.join(text.split())
    return text


def extract_json_text(json_path: str) -> Tuple[str, List[Dict]]:
    """Extract text from Screen Studio JSON transcript."""
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        transcript_items = data.get('json', {}).get('transcript', [])
        full_text = ' '.join([item.get('text', '') for item in transcript_items])

        return full_text, transcript_items
    except Exception as e:
        print(f"Error reading JSON {json_path}: {e}")
        return "", []


def extract_srt_text(srt_path: str) -> str:
    """Extract text from SRT file, ignoring timestamps and sequence numbers."""
    try:
        with open(srt_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # SRT format: sequence number, timestamp, text, blank line
        # Remove sequence numbers (lines that are just digits)
        # Remove timestamps (lines with -->)
        lines = content.split('\n')
        text_lines = []

        for line in lines:
            line = line.strip()
            # Skip empty lines, sequence numbers, and timestamps
            if not line or line.isdigit() or '-->' in line:
                continue
            text_lines.append(line)

        return ' '.join(text_lines)
    except Exception as e:
        print(f"Error reading SRT {srt_path}: {e}")
        return ""


def find_word_differences(original: str, corrected: str) -> List[Dict]:
    """Find significant word-level differences between texts."""
    orig_words = normalize_text(original).split()
    corr_words = normalize_text(corrected).split()

    matcher = SequenceMatcher(None, orig_words, corr_words)
    differences = []

    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == 'replace':
            differences.append({
                'type': 'changed',
                'original': ' '.join(orig_words[i1:i2]),
                'corrected': ' '.join(corr_words[j1:j2]),
                'position': i1
            })
        elif tag == 'delete':
            differences.append({
                'type': 'removed',
                'original': ' '.join(orig_words[i1:i2]),
                'corrected': '',
                'position': i1
            })
        elif tag == 'insert':
            differences.append({
                'type': 'added',
                'original': '',
                'corrected': ' '.join(corr_words[j1:j2]),
                'position': i1
            })

    return differences


def calculate_similarity(text1: str, text2: str) -> float:
    """Calculate similarity percentage between two texts."""
    norm1 = normalize_text(text1)
    norm2 = normalize_text(text2)
    return SequenceMatcher(None, norm1, norm2).ratio() * 100


def generate_report(results: List[Dict]) -> str:
    """Generate markdown report."""
    report = ["# Transcript Discrepancy Report\n"]
    report.append("**Generated:** " + Path(__file__).name + "\n")
    report.append("**Purpose:** Compare Screen Studio original transcripts with corrected SRT files\n")
    report.append("**Focus:** Semantic differences only (not punctuation, capitalization, or filler words)\n\n")

    report.append("---\n\n")
    report.append("## Summary\n\n")
    report.append("| Module | Similarity % | Significant Changes | Status |\n")
    report.append("|--------|-------------|---------------------|--------|\n")

    for result in results:
        status = "✅ Excellent" if result['similarity'] > 95 else "⚠️ Review" if result['similarity'] > 85 else "🔴 Major Changes"
        report.append(f"| {result['name']} | {result['similarity']:.1f}% | {len(result['differences'])} | {status} |\n")

    report.append("\n---\n\n")

    # Detailed findings per module
    for result in results:
        report.append(f"## Module: {result['name']}\n\n")
        report.append(f"**Similarity Score:** {result['similarity']:.1f}%\n\n")
        report.append(f"**Original Length:** {result['original_length']} words\n")
        report.append(f"**Corrected Length:** {result['corrected_length']} words\n")
        report.append(f"**Significant Differences Found:** {len(result['differences'])}\n\n")

        if not result['differences']:
            report.append("✅ **No significant discrepancies found.** The corrected SRT closely matches the original transcript.\n\n")
        else:
            report.append("### Discrepancies\n\n")

            # Limit to first 20 differences to avoid overwhelming output
            for i, diff in enumerate(result['differences'][:20], 1):
                report.append(f"**{i}. {diff['type'].upper()}** (position ~{diff['position']})\n")
                if diff['original']:
                    report.append(f"   - Original: `{diff['original']}`\n")
                if diff['corrected']:
                    report.append(f"   - Corrected: `{diff['corrected']}`\n")
                report.append("\n")

            if len(result['differences']) > 20:
                report.append(f"*... and {len(result['differences']) - 20} more differences*\n\n")

        # Recommendations
        report.append("### Recommendations\n\n")
        if result['similarity'] > 95:
            report.append("- ✅ SRT is highly accurate. Minimal review needed.\n")
        elif result['similarity'] > 85:
            report.append("- ⚠️ Good match overall. Review significant changes listed above.\n")
            report.append("- Check if semantic meaning is preserved in key sections.\n")
        else:
            report.append("- 🔴 Significant differences detected. Thorough review recommended.\n")
            report.append("- Verify that corrected content accurately reflects original speech.\n")
            report.append("- Consider spot-checking audio against both versions.\n")

        report.append("\n---\n\n")

    return ''.join(report)


def main():
    """Main execution function."""
    print("Starting transcript comparison analysis...\n")

    results = []

    for module in MODULES:
        print(f"Processing {module['name']}...")

        # Extract texts
        json_text, json_items = extract_json_text(module['json'])
        srt_text = extract_srt_text(module['srt'])

        if not json_text or not srt_text:
            print(f"  ⚠️  Could not read one or both files for {module['name']}")
            continue

        # Calculate similarity
        similarity = calculate_similarity(json_text, srt_text)

        # Find differences
        differences = find_word_differences(json_text, srt_text)

        # Store results
        results.append({
            'name': module['name'],
            'similarity': similarity,
            'original_length': len(normalize_text(json_text).split()),
            'corrected_length': len(normalize_text(srt_text).split()),
            'differences': differences
        })

        print(f"  Similarity: {similarity:.1f}% | Differences: {len(differences)}")

    # Generate report
    print("\nGenerating report...")
    report = generate_report(results)

    output_path = "/Users/matteolombardi/AI-Projects/stratega/stratega-academy/TRANSCRIPT_DISCREPANCY_REPORT.md"
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(report)

    print(f"\n✅ Report generated: {output_path}")


if __name__ == "__main__":
    main()
