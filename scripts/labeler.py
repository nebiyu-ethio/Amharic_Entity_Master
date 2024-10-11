import pandas as pd

class AmharicNERLabeler:

    def __init__(self):
        # Define keywords for different entities
        self.price_keywords = ['ዋጋ', 'ብር', 'ከ']
        self.location_list = [
            'አዲስ', 'የታይላንድ', 'ቦሌ', 'ቡልጋሪ', 
            'በረራ', 'ልደታ', 'ባልቻ', 'አአ'
        ]
        self.product_keywords = [
            'ምርት', 'ስቶቭ', 'ማንኪያ', 'የችበስመጥበሻ',
            'መጥበሻ', 'መጥበሻዎች', 'ምርቶች', 'ባትራ', 'ካርድ','መፍጫ',
            'መወልወያ','መደርደሪያ','መስታወት','እንጨት','ሶፋ','ኩርሲ'
        ]

    def label_tokens(self, tokens):

        labels = []

        for i, token in enumerate(tokens):
            token_stripped = token.strip()  # Strip any surrounding whitespace

            # Step 1: Check if the current token ends with "ብር"
            if token_stripped.endswith('ብር'):
                labels.append('I-PRICE')  # Label as I-PRICE
                continue
            
            # Step 2: Check if the current token is "ዋጋ"
            if token_stripped == 'ዋጋ':
                labels.append('B-PRICE')  # Label as B-PRICE
                continue
            
            # Step 3: Check if the current token is numeric
            if token_stripped.isdigit():
                # Check if the next token is "ብር"
                next_token = tokens[i + 1].strip() if i < len(tokens) - 1 else None
                if next_token == 'ብር':
                    labels.append('I-PRICE')  # Label as I-PRICE
                    continue

                # Check if the previous token is "ዋጋ"
                prev_token = tokens[i - 1].strip() if i > 0 else None
                if prev_token == 'ዋጋ':
                    labels.append('I-PRICE')  # Label as I-PRICE
                    continue
                else:
                    labels.append('O')  # Not a price entity
                    continue
            
            # Step 4: Check if the current token is "ብር"
            if token_stripped == 'ብር':
                # Check if the previous token is numeric
                prev_token = tokens[i - 1].strip() if i > 0 else None
                if prev_token and prev_token.isdigit():
                    labels.append('I-PRICE')  # Label as I-PRICE
                    continue
            
            # Step 5: Check if the current token contains both "ዋጋ" and "ብር"
            if 'ዋጋ' in token_stripped and 'ብር' in token_stripped:
                labels.append('I-PRICE')  # Label as I-PRICE
                continue
            
            # Step 6: Check if the current token contains "ከ" and "ብር"
            if 'ከ' in token_stripped and 'ብር' in token_stripped:
                labels.append('I-PRICE')  # Label as I-PRICE
                continue
            
            # Step 7: Check if the current token contains both "ዋጋ" and numeric values
            if 'ዋጋ' in token_stripped and any(char.isdigit() for char in token_stripped):
                labels.append('I-PRICE')  # Label as I-PRICE
                continue

            # Step 8: Check for location entities
            if token_stripped in self.location_list:
                labels.append('B-LOCATION')  # Label as B-LOC
                continue
            
            # Step 9: Check for product entities
            if token_stripped in self.product_keywords:
                labels.append('B-PRODUCT')  # Label as B-PROD
                continue

            # Step 10: Default case for tokens that are not part of any entities
            labels.append("O")  # Non-entity words

        return list(zip(tokens, labels))  # Return token-label pairs

    def label_dataframe(self, data, token_column):

        data['Labeled'] = data[token_column].apply(self.label_tokens)
        return data
    
    def save_conll_format(self, labeled_data, file_path):

        with open(file_path, 'w', encoding='utf-8') as f:
            for _, row in labeled_data.iterrows():
                for token, label in row['Labeled']:
                    f.write(f"{token} {label}\n")
                f.write("\n")  # Blank line between sentences/messages