package main

import (
	"errors"
	"fmt"
	"io/ioutil"
	"os"
	"path/filepath"
	"strconv"
	"strings"
)

func main() {
	args := os.Args
	if len(args) <= 2 {
		fmt.Printf("Error! Missing Files. \nKindly Add Input and Output Files.")
		return
	}
	inputFile := args[1]
	outputFile := args[2]
	_, err := os.Stat(inputFile)
	if err != nil {
		fmt.Println("File does not exist")
		return
	}
	data, err := ioutil.ReadFile(inputFile)
	if err != nil {
		fmt.Printf("File reading error, the input file is wrong.")
		return
	}
	if filepath.Ext(inputFile) != ".txt" || filepath.Ext(outputFile) != ".txt" {
		fmt.Printf("kindly add text files only such as sample.txt")
		return
	}
	if len(data) == 0 {
		fmt.Println("The file is empty.")
	}
	// change the string to array based on spaces
	words := strings.Fields(string(data))

	words, err = hexToDecimal(words)
	if err != nil {
		fmt.Println("Error: the word can not be changed to decimal")
	}
	words, err = binToDecimal(words)
	if err != nil {
		fmt.Println("Error: the word can not be changed to decimal")
	}
	words, err = toUp(words)
	if err != nil {
		fmt.Println(err)
	}
	words, err = toLow(words)
	if err != nil {
		fmt.Println(err)
	}
	words, err = toCap(words)
	if err != nil {
		fmt.Println(err)
	}
	words = vowels(words)
	strText := strings.Join(words, " ")
	punctuations := punctuations(strText)
	finalText := []byte(punctuations)
	ioutil.WriteFile(outputFile, finalText, 0)
}
func hexToDecimal(words []string) ([]string, error) {
	var err error
	var decimal_num int64
	for i := 0; i < len(words); i++ {
		if words[i] == "(hex)" {
			// change from hex to decimal
			decimal_num, err = strconv.ParseInt(words[i-1], 16, 64)
			if err == nil {
				words[i-1] = fmt.Sprint(decimal_num)
				words = append(words[:i], words[i+1:]...)
			}
		}
	}
	return words, err
}
func binToDecimal(words []string) ([]string, error) {
	var err error
	var decimal_num int64
	for i := 0; i < len(words); i++ {
		if words[i] == "(bin)" {
			// change from hex to decimal
			decimal_num, err = strconv.ParseInt(words[i-1], 2, 64)
			if err == nil {
				words[i-1] = fmt.Sprint(decimal_num)
				words = append(words[:i], words[i+1:]...)
			}
		}
	}
	return words, err
}
func toUp(words []string) ([]string, error) {
	var err error
	var count int
	for i := 0; i < len(words); i++ {
		if words[i] == "(up)" {
			if i-1 < len(words[:i]) {
				words[i-1] = strings.ToUpper(words[i-1])
				words = append(words[:i], words[i+1:]...)
			} else {
				err = errors.New("Error: nothing behind (up)")

			}
		}
		if words[i] == "(up," {
			count = changesCounter(words[i+1])
			position := i
			if count <= len(words[:i]) {
				for x := count; x > 0; x-- {
					words[position-1] = strings.ToUpper(words[position-1])
					position = position - 1
				}
				words = append(words[:i], words[i+2:]...)
			} else {
				err = errors.New("Error: the up count is bigger than the sentence")
			}
		}

	}
	return words, err
}

func toLow(words []string) ([]string, error) {
	var err error
	var count int
	for i := 0; i < len(words); i++ {
		if words[i] == "(low)" {
			if i-1 < len(words[:i]) {
				words[i-1] = strings.ToLower(words[i-1])
				words = append(words[:i], words[i+1:]...)
			} else {
				err = errors.New("Error: nothing behind (low)")
			}
		}
		if words[i] == "(low," {
			count = changesCounter(words[i+1])
			position := i
			if count <= len(words[:i]) {
				for x := count; x > 0; x-- {
					words[position-1] = strings.ToLower(words[position-1])
					position = position - 1
				}
				words = append(words[:i], words[i+2:]...)
			} else {
				err = errors.New("Error: the up count is bigger than the sentence")
			}
		}

	}
	return words, err
}
func toCap(words []string) ([]string, error) {
	var err error
	var count int
	for i := 0; i < len(words); i++ {
		if words[i] == "(cap)" {
			if i-1 < len(words[:i]) {
				words[i-1] = strings.Title(words[i-1])
				words = append(words[:i], words[i+1:]...)
			} else {
				err = errors.New("Error: nothing behind (cap)")
			}
		}
		if words[i] == "(cap," {
			count = changesCounter(words[i+1])
			position := i
			if count <= len(words[:i]) {
				for x := count; x > 0; x-- {
					words[position-1] = strings.Title(words[position-1])
					position = position - 1
				}
				words = append(words[:i], words[i+2:]...)
			} else {
				err = errors.New("Error: the up count is bigger than the sentence")
			}
		}

	}
	return words, err
}
func vowels(words []string) []string {
	vowels := []string{"a", "e", "i", "o", "u", "h", "A", "E", "I", "O", "U", "H"}
	for i := 0; i < len(words); i++ {
		if (words[i] == "A" || words[i] == "a") && i < len(words)-1 {
			switch words[i] {
			case "A":
				for _, vowel := range vowels {
					if strings.HasPrefix(words[i+1], vowel) {
						words[i] = "An"
					}
				}
			default:
				for _, vowel := range vowels {
					if strings.HasPrefix(words[i+1], vowel) {
						words[i] = "an"
					}
				}
			}

		}
	}
	return words
}

func punctuations(words string) string {
	// replace all the punctuations to be without spaces
	words = strings.ReplaceAll(words, " .", ".")
	words = strings.ReplaceAll(words, " ,", ",")
	words = strings.ReplaceAll(words, " !", "!")
	words = strings.ReplaceAll(words, " ?", "?")
	words = strings.ReplaceAll(words, " :", ":")
	words = strings.ReplaceAll(words, " ;", ";")
	words = strings.ReplaceAll(words, " '", "'")
	words = strings.ReplaceAll(words, "' ", "'")
	words = strings.ReplaceAll(words, "‘ ", "‘")
	words = strings.ReplaceAll(words, " ’", "’")

	// check if the punctuation is followed with a letter then leave a space
	for index, letter := range words {
		if (letter == '.' || letter == ',' || letter == '!' || letter == '?' || letter == ':' || letter == ';') && index+1 < len(words) {
			if (words[index+1] >= 'A' && words[index+1] >= 'Z') || (words[index+1] >= 'a' && words[index+1] >= 'z') {
				words = words[:index+1] + " " + words[index+1:]
			}
		}
	}
	// arrange the spacing for the '
	first := true
	firstOtherQuote := true
	for index := 0; index < len(words); index++ {
		if string(words[index]) == "'" {
			if first {
				words = words[:index] + " " + words[index:]
				first = false
				index = index + 1
			} else {
				words = words[:index+1] + " " + words[index+1:]
				first = true
			}
		}
		if string(words[index]) == "‘" || string(words[index]) == "’" {
			if firstOtherQuote {
				words = words[:index] + " " + words[index:]
				firstOtherQuote = false
				index = index + 1
			} else {
				words = words[:index+1] + " " + words[index+1:]
				firstOtherQuote = true
			}
		}
	}
	return words
}

// get the streing for example 10) and extract the number to return it as integer
func changesCounter(word string) int {
	strNum := ""
	number := 0
	for _, charecter := range word {
		if charecter >= '0' && charecter <= '9' {
			number = int(charecter - '0')
			strNum = strNum + strconv.Itoa(number)
		}
	}
	count, _ := strconv.Atoi(strNum)
	return count
}
