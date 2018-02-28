# Report for assignment 4

## Project

Name: Hypothesis

URL: https://github.com/FrancoisChastel/h

This repository is a web app api that helps with web annotations.

## Complexity

1. What are your results for the 8 most complex functions?

A) h/routes.py : The complexity of the function is due to their binding strategy and the complexity should be high. 

   Lizard Tool Complexity Measure: https://github.com/FrancoisChastel/h/blob/testCoverageFix/routes_lizard_output.txt

   Hand Complexity Measure: 

B) h/panels/navbar.py : The complexity of the function is due to their building strategy and the complexity shouldn’t be high.

   Lizard Tool Complexity Measure: https://github.com/FrancoisChastel/h/blob/testCoverageFix/navbar_lizard_output.txt

   Hand Complexity Measure: 

C) h/config.py : The complexity of the function is due to their binding strategy and the complexity should be high.

   Lizard Tool Complexity Measure: https://github.com/FrancoisChastel/h/blob/testCoverageFix/config_lizard_output.txt

   Hand Complexity Measure: 

D) h/util/redirects.py : The function is parse and it have to be that complex to deal with different cases.

   Lizard Tool Complexity Measure: https://github.com/FrancoisChastel/h/blob/testCoverageFix/redirects_lizard_output.txt

   Hand Complexity Measure: 

E) h/streamer/messages.py : The complexity of the function is due to their binding strategy and the complexity should be high.

   Lizard Tool Complexity Measure: https://github.com/FrancoisChastel/h/blob/testCoverageFix/streamer_lizard_output.txt

   Hand Complexity Measure: 

F) /h/accounts/schemas.py serialize(self, node, appstruct): Complexity due to different cases of user being invalid or reset code being invalid. Complexity shouldn't be high. 

   Lizard Tool Complexity Measure: https://github.com/FrancoisChastel/h/blob/testCoverageFix/schemas_lizard_output.txt

   Hand Complexity Measure: 

G) /h/accounts/schemas.py deserialize(self, node, cstruct): Complexity due to reset code having various states, such as invalid and nonexistent. In order to accomodate for all these cases, the complexity must be high.  
 
   Lizard Tool Complexity Measure: https://github.com/FrancoisChastel/h/blob/testCoverageFix/schemas_lizard_output.txt

   Hand Complexity Measure: 

H) h/services/__init__.py : The complexity of the function is due to their binding strategy and the complexity should be high.

   Lizard Tool Complexity Measure: https://github.com/FrancoisChastel/h/blob/testCoverageFix/init_lizard_output.txt

   Hand Complexity Measure:

2. Are the functions just complex, or also long?

The functions routes, __init__ and config are long function but not especially complex compare to the navbar function that is little more complex. The functions in schemas.py , redirects.py and messages.py are not very long; the length mainly comes from many if statements for many different cases. 

3. What is the purpose of the functions?
h/routes.py : This function aim to map the APIs routes and the python's function inside the project.

h/services/__init__.py : This function aim to init the services of the hypothesis. 

h/panels/navbar.py : Create the binding and the elements of the navbar with the bind linked with api routes

h/config.py : Configure the whole application project.

h/util/redirects.py : Parse a list of redirects from a sequence of redirect specifiers.

h/streamer/messages.py : Get message about annotation event to be sent to socket.

h/accounts/schemas.py serialize(self, node, cstruct): transforms a reset code into form used by User

/h/accounts/schemas.py serialize(self, node, cstruct): transforms reset code from user into object used by program

4. Are exceptions taken into account in the given measurements?
No.

5. Is the documentation clear w.r.t. all the possible outcomes?
Yes.


## Coverage

### Tools

Document your experience in using a "new"/different coverage tool.

How well was the tool documented? Was it possible/easy/difficult to
integrate it with your build environment?

It was easy to run a test coverage tool on their project regarding the fact they have their own tool. After using another tool as recommend it really easy and fast to use regarding we need only two commands to run the test coverage.

### DYI


Show a patch that show the instrumented code in main (or the unit test setup), and the 8 methods where branch coverage is measured.


Eight Functions:
In some cases, we used entire files instead of functions due to the high modularity of functions in this application. In those cases, choosing only functions would have yielded too little work. 

search/client.py

search/parser.py

search/index.py

seatch/query.py

accounts/schemas.py serialize(self, node, appstruct):

accounts/schemas.py deserialize(self, node, cstruct):

util/redirects.py parse(specs):

streamer/messages.py _generate_annotation_event(message, socket, annotation, user_nipsad, group_service):

The patch is probably too long to be copied here, so please add the git command that is used to obtain the patch instead:

git diff ...

What kinds of constructs does your tool support, and how accurate is its output?



### Evaluation

1. Report of old coverage: https://github.com/FrancoisChastel/h/blob/1c0f9ca61efa35df4fcfdc6682f0969c64f422aa/before_coverage.log

2. Report of new coverage: https://github.com/FrancoisChastel/h/blob/579ca83b5a16c304f29e90080321547e95e08df4/after_coverage.log

3. Test cases added:
	
Many of our files had 100% test coverage, thus we analyzed how that came to be and its difference with path coverage. So, not everyone was able to write a lot of tests in order to improve the already very high test coverage.

test_replies_matcher (query_test.py)

test_invalid_input (query_test.py)

test_if_unique_username (schemas_test.py)

testIncludeMe (schemas_test.py)

test_serialize_reset_code (schemas_test.py)

test_deserial_new_user (schemas_test.py)

test_normal_add_unknown_type (redirects_test.py)

test_comment_add_multilines (redirects_test.py)


## Refactoring
h/routes.py : this function is pretty hard to lower down his complexity regarding the fact we are defining the routes for the api a way to lower down the cost could be to generate an automatic binding between the services and the api access programmatically without hardcoding it 
h/services/__init__.py : this function suffer from for the same issue than routes.py, it’s about binding to lower down the complexity we could have an automatic binding of the factory and not hardcoding it 
h/panels/navbar.py : this function suffer from a high complexity in term of code purity because they didn’t divided the behaviour of the function in different aspect of the function, they could have a function for each behaviour 
h/config.py : the complexity of their function is almost systematically suffering from the same issue : a lot of binding.


## Effort spent

For each team member, how much time was spent in

1. plenary discussions/meetings;
	All members: 3 hours

2. discussions within parts of the group;
	All members: 2 hours

3. reading documentation;
	Brian: 5
	Anu: 4
	Francois: 4
	Jiayu: 4

4. configuration;
	Brian: 2
	Anu: 3
	Francois: 5
	Jiayu: 4

5. analyzing code/output;
	Brian: 7
	Anu: 10
	Francois: 8
	Jiayu: 9

6. writing documentation;
	Brian: 4
	Anu: 3
	Francois: 2
	Jiayu: 1

7. writing code;
	Brian: 8 (xp with François)
	Anu: 9
	Francois: 8 (xp with Brian)
	Jiayu: 9

8. running code?
	Brian: 7 (xp with François)
	Anu: 5
	Francois: 5 (xp with Brian)
	Jiayu: 6


## Overall experience

Overall, this project was very interesting. It allowed our group to really dive into the testing aspect of software engineering. We were able to see some really good testing methods, and some really not so good testing methods. This repo had some very efficient code in it, which meant it had many small functions with few nodes and extremely high test coverage. Many of our selected files had almost 100%, if not 100%, test coverage on them. This made it very difficult to increase the test coverage, as many of the unreached nodes were from unused functions, or wasteful code. In the end, this offered our group a unique experience to critique and explore a good example of an open source library for their testing practices.
