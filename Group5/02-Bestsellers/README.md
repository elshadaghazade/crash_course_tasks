# Bestsellers

## Assignment Overview

This assignment focuses on the design, implementation and testing of a Python program which uses file processing, lists and strings to solve the problem described below.

## Assignment Specifications

The New York Times newspaper has published “best seller” lists since 1942.  Book sales are tracked nationwide, leading to a list of those books which have recently sold the most copies.

You will design, implement and test a program which allows the user to search a subset of the books which have appeared in the New York Times best seller lists.  For simplicity, the data set will only contain those books which have reached #1 on either of two lists (fiction and nonfiction) since 1942.

The file named bestsellers.txt contains the data set.  Each line of the file contains the information for a separate book, which includes:  title, author, publisher, date it first reached #1 on one of the best seller lists, and category (fiction or nonfiction).  There is a tab character between fields.

The program will input the data set and construct a list of books.  If the list of books cannot be constructed, the program will display an appropriate error message and halt.

After constructing the list of books, the program will display a menu of options and allow the user to search for books which meet certain criteria.  The menu options are:

1. Display all books in a year range:  Prompt the user for two years (a starting year and an ending year), then display all books which reached the #1 spot between those two years (inclusive).  For example, if the user entered “1970” and “1973”, display all books which reached #1 in 1970, 1971, 1972 or 1973.

2. Display all books in a specific month and year:  Prompt the user to enter a month and year, then display all books which reached #1 during that month.  For example, if the user entered “7” and “1985”, display all books which reached #1 during the month of July in 1985.

3. Search for an author:  Prompt the user for a string, then display all books whose author’s name contains that string (regardless of case).  For example, if the user enters “ST”, display all books whose author’s name contains (or matches) the string “ST”, “St”, “sT” or “st”.

4. Search for a title:  Prompt the user for a string, then display all books whose title contains that string (regardless of case).  For example, if the user enters “secret”, three books are found:  “The Secret of Santa Vittoria” by Robert Crichton, “The Secret Pilgrim” by John le Carré, and “Harry Potter and the Chamber of Secrets”.

## Assignment Notes

1.  Your program will consist of at least four functions:  a separate function to process each of the four menu options listed above.

2.  You may lists and tuples in your program, but you may not use other collections (such as a dictionary or map).

3.  Be sure to display the books in a reasonable and readable manner.

4.  If no books are found for a particular search, your program will display an appropriate message (rather than simply displaying nothing).

5.  Your program will continue to execute until the user selects “Q” (or “q”) as the menu option.

6.   Be sure to prompt the user for the inputs in the specified order.  Also, your program cannot prompt the user for any other inputs.

7.  Your program will handle erroneous user inputs.  If there are any problems with a particular user input, your program will display the menu and allow the user to select another option.


## Sample Output:


```console
What would you like to do?
1: Look up year range
2: Look up month/year
3: Search for author
4: Search for title
Q: Quit
>1
  Enter beginning year: 1960
  Enter ending year: 1962

All Titles between 1960 and 1962 :
   A Shade of Difference, by Allen Drury (10/28/1962)
   Franny and Zooey, by J. D. Sallinger (10/29/1961)
   Hawaii, by James Michener (1/17/1960)
   Seven Days in May, by Fletcher Knebel (11/18/1962)
   Ship of Fools, by Katherine Anne Porter (4/29/1962)
   The Agony and the Ecstasy, by Irving Stone (4/23/1961)
   The Last of the Just, by André Schwarz-Bart (3/26/1961)
   Born Free, by Joy Adamson (8/7/1960)
   Calories Don't Count, by Herman Taller (3/25/1962)
   May This House Be Safe from Tigers, by Alexander King (3/13/1960)
   Silent Spring, by Rachel Carson (10/28/1962)
   The Making of the President - 1960, by Theodore H. White (9/10/1961)
   The New English Bible, by Oxford University Press (Editor) (5/28/1961)
   The Rise and Fall of the Third Reich, by William Shirer (12/4/1960)
   The Rothchilds, by Frederic Morton (6/24/1962)
   The Waste Makers, by Vance Packard (11/6/1960)
   Travels with Charley, by John Steinbeck (10/21/1962)

What would you like to do?
1: Look up year range
2: Look up month/year
3: Search for author
4: Search for title
Q: Quit
>2
  Enter month (as a number, 1-12): 9
  Enter year: 1990

All Titles in month 9 of 1990 :
   Four Past Midnight, by Stephen King (9/16/1990)
   Memories of Midnight, by Sidney Sheldon (9/2/1990)
   Darkness Visible, by William Styron (9/16/1990)
   Millie's Book, by Barbara Bush (9/30/1990)
   Trump: Surviving at the Top, by Donald Trump (9/9/1990)

What would you like to do?
1: Look up year range
2: Look up month/year
3: Search for author
4: Search for title
Q: Quit
>3
  Enter an author's name (or part of a name): tolkein
   Silmarillion, by J. R. R. Tolkein (10/2/1977)
   The Children of the Húrin, by J.R.R. Tolkein (5/6/2007)

What would you like to do?
1: Look up year range
2: Look up month/year
3: Search for author
4: Search for title
Q: Quit
>4
  Enter a title (or part of a title): secret
   Harry Potter and the Chamber of Secrets, by J. K. Rowling (6/20/1999)
   The Secret of Santa Vittoria, by Robert Crichton (11/20/1966)
   The Secret Pilgrim, by John le Carré (1/20/1991)
```