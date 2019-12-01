# Stringo

### An Open Source Python Library that includes some pre-coded functions which can be applied for different type of string/text operations accordingly.

##### The main idea behind coding this library was to facilitate the programmer to perform simple strings operations without have to worry about the datatype such as simple single string, list of strings, Series or DataFrame. 


## Available Functions

* [apply_function_typewise](#apply_function_typewise)
* [lemmatize_object](#lemmatize_object)
* [stem_object](#stem_object)
* [remove_extra_spaces](#remove_extra_spaces)
* [split_sentences_spacy](#split_sentences_spacy)
* [remove_punctuations](#remove_punctuations)
* [remove_empty_from_list](#remove_empty_from_list)
* [sort_list_of_strings](#sort_list_of_strings)
* [tokenize_string_spacy](#tokenize_string_spacy)

## Usage

#### For Demo Purpose I am going to use the following examples:

```python
simple_string = "I am a Programmer  !"
list_of_strings = ["I am a Programmer  !", "@I love to Code"]
dataframe = pd.DataFrame(["I am a Programmer  ", "I love to Code."], columns=['strings'])
series = pd.Series(["I am a Programmer!!!", "I love to Code...  ..."])
```

# <a href='stem_object'>stem_object</a>

```
print ('Simple String : \n', stem_object(simple_string))
print ('---------- \nList of Strings : \n', stem_object(list_of_strings))
print ('---------- \nDataFrame : \n', stem_object(dataframe))
print ('---------- \nSeries: \n', stem_object(series))

======== OUTPUT =============>

Simple String: 
 i am a programmer  !
---------- 
List of Strings: 
 ['i am a programmer  !', '@i love to cod']
---------- 
DataFrame: 
                strings
0  i am a programmer  
1      i love to code.
---------- 
Series: 
0      i am a programmer!!!
1    i love to code...  ...

```
