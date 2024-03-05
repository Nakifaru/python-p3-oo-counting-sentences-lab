#!/usr/bin/env python3

class MyString:
  def __init__(self, value=''):
    self.value = value

  @property
  def value(self):
    return self._value
  
  @value.setter
  def value(self, value):
    if isinstance(value, str):
      self._value = value
    else:
      print("The value must be a string.")
  
  def is_sentence(self):
    return self.value.endswith('.')
  
  def is_question(self):
    return self.value.endswith('?')

  def is_exclamation(self):
    return self.value.endswith('!')
  
  def count_sentences(self):
    partially_replaced =self.value.replace('!', '.')
    fully_replaced = partially_replaced.replace('?', '.')
    split_sentences = fully_replaced.split('.')
    non_empty_sentences = list(filter(None, split_sentences))
    return len(non_empty_sentences)
  




