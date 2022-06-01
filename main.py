# Adrian, Lam (705929)
# ICS4U-A Assignment: Data Structures and Algorithms (J. Garvin)
# Date: 05-31-2022
#
# Program opens desired HTML file or document, reads it, then displays HTML blocks.
# Program uses a stack to parse data from the HTML document. Exceptions and program
# crashes are also handled. Program does NOT support correct HTML attributes/elements/tags,
# and is only used for checking HTML tags/blocks that are wrongly formatted. Program
# handles cases where some HTML tags do not containing closing pairs such as HTML image
# attributes/elements. Program is able to handle cases where HTML blocks and tags all reside
# in the same line (without indents).
#
# FUTURE IMPLEMENTATIONS:
# - correct names for HTML tags/elements/attributes
# - formatting HTML documents/files similar to a module called BeautifulSoup (BS)
#
# EDIT:
# - slight change regarding comments (mainly program description)
# - minor code changes

# imports and initial vals
import time

time_start = time.time()  # get time at current moment

# functions
# open_file function for opening and reading html files
def open_file(file_name):
    L = []  # initial list
    try:
        with open(file_name, "r") as input_file:  # open file
            # iterating through lines/elements of file
            for elem in input_file:
                elem = elem.strip()  # stripping whitespace
                L.append(elem)  # appending elements in input_file (lines) to list
    except FileNotFoundError:  # exception for File Not Found Error
        print("File not found.")
    except:  # unknown exceptions and crashes
        print("Unknown error occurred.")
    return L  # returns the initial list


# time function for counting // duration of program execution
def time_counter(time_start):
    time_now = time.time()  # get time at current moment
    delta_time = (time_now - time_start) * 1000  # converting time to milliseconds
    delta_time = round(delta_time, 3)  # rounding time to 3 dec-places
    return delta_time  # returning delta time value


# function for finding tags // main function for sorting and finding unclosed tags/blocks
def find_tag():
    L = open_file("example4.html")  # desired file to open // filename
    tag_stack = []  # defining tag stack / list
    # reiterating through elements of L to find strings
    for elem in L:
        if not "<" in elem:  # if element contains "<"
            L.remove(elem)  # remove element from list
    # reiterating through elements of L to find blocks and tags
    for elem in L:
        opening_num = elem.count(
            "<"
        )  # determine number of opening/closed tags or blocks
        # loop for number of opening/closed tags or blocks in current line/element
        for iter in range(opening_num):
            if iter == 0:  # if current value is 0
                left_tag = elem.find("<")  # find index of "<" in elem
                if left_tag > -1:  # if "<" is found
                    right_tag = elem.find(">")  # find index of ">" in elem
                    if right_tag > -1:  # if ">" is found
                        html_tag = elem[left_tag + 1 : right_tag]  # string slicing
                    else:  # if ">" is not found."
                        print(f"End tag for {html_tag} not found.")
                else:  # if "<" is not found."
                    print(f"Start tag for {html_tag} not found.")
            else:  # if more than 1 tag is found in the same line
                start = right_tag + 1  # value to the right of the right tag (">")
                left_tag = elem.find(
                    "<", start
                )  # 'start' determines where .find function will start searching for the index of "<"
                right_tag = elem.find(
                    ">", start
                )  # 'start' determines where .find function will start searching for the index of ">"
                html_tag = elem[left_tag + 1 : right_tag]  # string slicing
            if (
                html_tag[0] != "/" and html_tag[-1] != "/"
            ):  # if first or last char of html_tag does not contain "/"
                tag_stack.append(html_tag)  # add html tag to tag stack
            else:  # if html_tag contains "/"
                html_tag = html_tag[1:]  # take values/chars after "/"
                if (
                    tag_stack[-1] == html_tag
                ):  # if previous tag_stack value is the same as html_tag
                    tag_stack.pop()  # pop previous tag_stack value
    return tag_stack  # return the stack or list of tags // incorrect or wrongly formatted tags in html file


# info function for displaying stats and results
def main():
    tag_stack = find_tag()  # all the find_tag function
    if len(tag_stack) == 0:  # if the length of the tag_stack is 0
        print("HTML file is formatted correctly.")
    else:  # if the length of the tag_stack is > 0
        print("HTML file is formatted incorrectly.")
    print(
        "Program finished in:", time_counter(time_start), "ms."
    )  # displays time since program execution


# main program
main()
