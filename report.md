# Report for assignment 4

## Project

Name: Hypothesis

URL: https://github.com/FrancoisChastel/h

This repository is a web app api that helps with web annotations.

## Complexity

1. What are your results for the ten most complex functions?

h/routes.py : The complexity of the function is due to their binding strategy and the complexity should be high. 

h/services/__init__.py : The complexity of the function is due to their binding strategy and the complexity should be high. 

h/panels/navbar.py : The complexity of the function is due to their building strategy and the complexity shouldn’t  be high.

/h/config.py : The complexity of the function is due to their binding strategy and the complexity should be high.

2. Are the functions just complex, or also long?
The functions routes __init__ and config are long function but not especially complex compare to the navbar function that is little more complex.

3. What is the purpose of the functions?
h/routes.py : This function aim to map the APIs routes and the python's function inside the project.

h/services/__init__.py : This function aim to init the services of the hypothesis. 

h/panels/navbar.py : Create the binding and the elements of the navbar with the bind linked with api routes

/h/config.py : Configure the whole application project.

4. Are exceptions taken into account in the given measurements?
No.

5. Is the documentation clear w.r.t. all the possible outcomes?
Yes.


## Coverage

### Tools

Document your experience in using a "new"/different coverage tool.

How well was the tool documented? Was it possible/easy/difficult to
integrate it with your build environment?

### DYI


Show a patch that show the instrumented code in main (or the unit test setup), and the ten methods where branch coverage is measured.


Eight Functions:
We selected 8 files to use rather than functions due to the efficiency of the code we have. Using 8 functions would not have yielded enough work.

search/client.py

search/parser.py

search/index.py

seatch/query.py

The patch is probably too long to be copied here, so please add the git command that is used to obtain the patch instead:

git diff ...

What kinds of constructs does your tool support, and how accurate is its output?



### Evaluation

1. Report of old coverage: [link]

2. Report of new coverage: [link]

3. Test cases added:
	
Many of our files had 100% test coverage, thus we analyzed how that came to be and its difference with path coverage. So, not everyone was able to write a lot of tests in order to improve the already very high test coverage.

test_replies_matcher (query_test.py)

test_invalid_input (query_test.py)



## Refactoring
h/routes.py : this function is pretty hard to lower down his complexity regarding the fact we are defining the routes for the api a way to lower down the cost could be to generate an automatic binding between the services and the api access programmatically without hardcoding it 
h/services/__init__.py : this function suffer from for the same issue than routes.py, it’s about binding to lower down the complexity we could have an automatic binding of the factory and not hardcoding it 
h/panels/navbar.py : this function suffer from a high complexity in term of code purity because they didn’t divided the behaviour of the function in different aspect of the function, they could have a function for each behaviour 
/h/config.py : the complexity of their function is almost systematically suffering from the same issue : a lot of binding.


## Effort spent

For each team member, how much time was spent in

1. plenary discussions/meetings;
	All members: 3 hours

2. discussions within parts of the group;
	All members: 2 hours

3. reading documentation;
	Brian: 5
	Anu:
	Francois:
	Jiayu:

4. configuration;
	Brian: 2
	Anu:
	Francois:
	Jiayu:

5. analyzing code/output;
	Brian: 7
	Anu:
	Francois:
	Jiayu:


6. writing documentation;
	Brian: 4
	Anu:
	Francois:
	Jiayu:


7. writing code;
	Brian: 8
	Anu:
	Francois:
	Jiayu:


8. running code?
	Brian: 7
	Anu:
	Francois:
	Jiayu:


## Overall experience

Overall, this project was very interesting. It allowed our group to really dive into the testing aspect of software engineering. We were able to see some really good testing methods, and some really not so good testing methods. This repo had some very efficient code in it, which meant it had many small functions with few nodes and extremely high test coverage. Many of our selected files had almost 100%, if not 100%, test coverage on them. This made it very difficult to increase the test coverage, as many of the unreached nodes were from unused functions, or wasteful code. In the end, this offered our group a unique experience to critique and explore a good example of an open source library for their testing practices.
