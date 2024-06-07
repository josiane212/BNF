import gensim.models
from gensim.models import Word2Vec, KeyedVectors
import os
from gensim.test.utils import datapath

### Menu that the user will choose from ###

main_menu = ("Please select what you want to find out :\n" +
                "\t1. Similarity between terms\n\n" +
                "\t2. Most similar word to a term\n" +
                "\t3. Operations/analogies on vectors\n" +
                "\t4. Which doesn't belong?\n"
                "\t5. End program\n")

menu_stop = 5

#//////////////////////////////////
#                                #
##           FUNCTIONS          ##
#                                #
#//////////////////////////////////

######################################
#Fetch model
def model_loading(model_name) :
    return Word2Vec.load(model_name)

#/#/#/#/#/#/#/#/#/#/#/#
# Print the query information and result, to view them immidiately
def print_query(query_intro, final_result):
    print("===============================")
    print(query_intro)
    print(final_result)
    print("===============================\n")

#|#/#/#/#/#/#/#/#/#/#/#/#
#| Check the similarity of a given pair of terms (if terms are in model)
#| Also prints the result, adds it to the text file
#| and appends the pair to a list of pairs
def pair_similarity(model, term_1, term_2):
    pair_intro = ("Similarity between : " + term_1 + " & " + term_2 + "\n")
    try:
        simil = model.wv.similarity(term_1, term_2) * 100
    except:
        print("\n---------\nOne of the term entered is not in the vectorized corpus. Please try again")
    else:
        print_query(pair_intro, simil)  
        return simil

#|#/#/#/#/#/#/#/#/#/#/#/#
#| Check the most similar terms of a given term (if term is in model)
#| Also prints the result, adds it to the text file
#| and appends the term to a list of terms
def most_simil(model, term, top_n):
    mostSimil_intro = ("Top " + str(top_n) + " most similar terms to : " + term + "\n")
    try:
        mostSimil_terms = model.wv.most_similar(term, topn=top_n)
    except:
        print(f"\n---------\n -- {term} -- is not in the vectorized corpus. Please try again")
    else:
        print_query(mostSimil_intro, mostSimil_terms)
        return mostSimil_terms

#|#/#/#/#/#/#/#/#/#/#/#/#
#| Apply operations on vectors (if vectors are in model)
#| Always the same operation here : term1 - term2 + term3
#| Also prints the result, adds it to the text file
#| and appends the terms to the operation_list
def oper_time(model, term_uno, term_dos, term_tres):
    operTime_intro = term_uno + " - " + term_dos + " + " + term_tres + " = \n"
    try:
        operation = model.wv.most_similar(positive=[term_uno, term_tres], negative=[term_dos], topn=3)
    except:
        print("\n---------\nOne of the term entered is not in the vectorized corpus. Please try again")
    else:     
        print_query(operTime_intro, operation)
        return operation

#|#/#/#/#/#/#/#/#/#/#/#/#
#| Check the odd vector in a list of vectors (if vectors are in model)
#| Also prints the result, adds it to the text file
#| and appends the terms to the odd_list
def odd_one_out(model, list_of_terms) :
    odd_one_intro = "Here is the odd term out of the provided list which goes as this : " + ", ".join(list_of_terms)
    try:
        odd_one = "\n--> " + str(model.wv.doesnt_match(list_of_terms))
    except:
        print("\n---------\nOne of the term entered is not in the vectorized corpus. Please try again")
    else:
        print_query(odd_one_intro, odd_one)
        return odd_one

#|#/#/#/#/#/#/#/#/#/#/#/#
#| Evaluating analogies (if vectors are in model)
#| Also prints the result, adds it to the text file
#| and appends the terms to the odd_list
#def evaluation(file)

#//////////////////////////////////
#                                #
##      Interaction Start       ##
#                                #
#//////////////////////////////////

# User input to decide what to check
def start_interface(path_to_model) :
    model = model_loading(path_to_model)
    menu_choice = int(input(main_menu))
    if menu_choice > menu_stop :
        print("You entered a number that was not in the menu. -_-. #1 to #4 only. Please start the program again.")

    ##############
    # Loop start
    while menu_choice < menu_stop :
        
    #--------------
    # Choice 1 : Similarity between terms
        if menu_choice == 1 :
            #| Enter the first term of the pair. The user can enter
            #| pair_list to check the pre-made "pairs" list, 
            first_term = input("Enter the fist term : ").lower()
            second_term = input("Enter the second term : ").lower()
            pair_similarity(model, first_term, second_term)

    #--------------
    # Choice 2 : Most n similar word to a term
        elif menu_choice == 2 :
            #| Enter the term. The user can enter
            #| term_list to check the pre-made "terms" list,         
            term_check = input("Which term do you want to check: ").lower()
            
            # The user can enter the number of results they want
            n_check = int(input("Top n most similar terms... n = "))

            most_simil(model, term_check, n_check)

    #--------------
    # Choice 3 : Operations on terms           
        elif menu_choice == 3 :
        
            print("For now, operations are Term1 - Term2 + Term3. ")
            #| Enter the term. The user can enter
            #| op_list to check the pre-made "terms" list, 
            #| or "otzie" to trigger the one written in code beforehand.
            first_add = input("Term 1 : ")
            second_add = input("- Term 2 : ")
            third_add = input("+ Term 3 : ")

            oper_time(model, first_add, second_add, third_add)

    #--------------
    # Choice 4 : Operations on terms
        elif menu_choice == 4 :
            temp_list = []
            first_item = input("This option lets you find the odd one out of a list. Enter 'stop' at any number (but the First one) when you want to end the list. \nPlease enter the first term you want to add to the list : ")

            temp_list.append(first_item)
            number = 2
            new_item = input("Term #" + str(number) + " : ")
            while new_item.lower() != "stop" :
                temp_list.append(new_item)
                number += 1
                new_item = input("Term #" + str(number) + " : ")
            odd_one_out(model, temp_list)
               
    #--------------
    # PROMPTING USER for loop or stop loop  
        menu_choice = int(input(main_menu))