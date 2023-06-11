class VigenaireСipher:
    ALPHABET_START = ord('А')
    ALPHABET_LEN = 66
    
    def encrypting(self, text: str, key: str, iterations: int = 1):
        len_text_without_spaces = len(text.strip().replace(' ', ''))
        cipher_key = self._fill_key_to_text_len(key, len_text_without_spaces)
        words = text.split()
        for _ in range(iterations):
            words = self._encrypt_words(words, cipher_key)
        return ' '.join(words)

    def decrypting(self, text: str, key: str, iterations: int = 1):
        len_text_without_spaces = len(text.strip().replace(' ', ''))
        cipher_key = self._fill_key_to_text_len(key, len_text_without_spaces)
        words = text.split()
        for _ in range(iterations):
            words = self._decrypt_words(words, cipher_key)
        return ' '.join(words)

    def _encrypt_words(self, words: list[str], key: str):
        encrypted_words = []
        key_index = 0
        for word in words:
            encrypt_key = key[key_index:key_index+len(word)]
            encrypted_words.append(self._encrypt_word(word, encrypt_key))
            key_index = key_index + len(word)
        return encrypted_words

    def _encrypt_word(self, word: str, key: str):
        encrypted_text = ''
        for index, char in enumerate(word):
            char_num = ord(char) - self.ALPHABET_START
            key_num = ord(key[index]) - self.ALPHABET_START
            encrypted_num = (char_num + key_num) % self.ALPHABET_LEN
            encrypted_char = chr(encrypted_num + self.ALPHABET_START)
            encrypted_text += encrypted_char
        return encrypted_text
    
    def _decrypt_words(self, words: list[str], key: str):
        decrypted_words = []
        key_index = 0
        for word in words:
            encrypt_key = key[key_index:key_index+len(word)]
            decrypted_words.append(self._decrypt_word(word, encrypt_key))
            key_index = key_index + len(word)
        return decrypted_words

    def _decrypt_word(self, word: str, key: str):
        decrypted_text = ''
        for index, char in enumerate(word):
            char_num = ord(char) - self.ALPHABET_START
            key_num = ord(key[index]) - self.ALPHABET_START
            decrypted_num = (char_num - key_num) % self.ALPHABET_LEN
            decrypted_char = chr(decrypted_num + self.ALPHABET_START)
            decrypted_text += decrypted_char
        return decrypted_text

    
    def _fill_key_to_text_len(self, key: str, text_len: int) -> str:
        if text_len < len(key):
            return key[:text_len]

        key_word_count = text_len // len(key)
        key_word_residue = text_len % len(key)
        return key * key_word_count + key[:key_word_residue]
    

