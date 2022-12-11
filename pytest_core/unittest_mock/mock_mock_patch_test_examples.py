from unittest.mock import Mock, patch
def complex_function():
    return "foo"

def function_a():
    return complex_function().upper()


# TODO: Test1: test function_a, use patch to mock complex_function
#       Test2: test if complex_function in patch was called
##### Your test here 

def test_function_a():
    with patch('mock_mock_patch_test_examples.complex_function') as mock:
        mock.return_value = "foo"
        function_a_return = function_a()
        assert function_a_return == "FOO"
        mock.assert_called
#####

class MyClass:
    def __init__(self, name):
        self.name = name

    def sayhi(self):
        return "hi my name is: {}".format(self.name)

# instantiates MyClass and calls a method on the object
def function_b():
    param1 = MyClass("foo")

    # returns "hi my name is: foo"
    return param1.sayhi()

# TODO: Test2: test function_b, use with patch.object 
##### Your test here 
def test_functio_b():
    #(ProductionClass, 'method', return_value=None)
    with patch.object(MyClass, 'sayhi', return_value = "hi my name is foo") as mock:
        function_b_return = function_b()
        assert function_b_return == "hi my name is foo"
#####


def function_with_call(some_obj, argument):
    return some_obj.some_method(argument)

# TODO: Test3: test function_with_call, use mock.methodss.assert_called() to 
# see if method was actually called once or more 
#       Test3.1: use assert_called_with to check if method was called correct    argument 
##### Your test here
def test_function_with_call():
    mock = Mock()
    mock.return_value.some_method = Mock(return_value=None, autospec=True)
    function_with_call(mock, 'a')
    mock.some_method.assert_called()
    mock.some_method.assert_called_with('a')
#####


# this function takes both params, modifies them and send to 
# complex_function_with_params
def complex_function_with_params(a, b):
    return a + b

def function_e(param1, param2):
    return complex_function_with_params(param1.upper(), param2.upper())

# TODO: Test4: use patch and assert_called_with 
##### Your test here 
@patch('mock_mock_patch_test_examples.complex_function_with_params')
def test_function_e(mock):
    function_e_return = function_e('a', 'b')
    mock.assert_called_with('A', 'B')
#####

def function_c(param):
    output = param.sayhi()

    return output.upper()


# TODO: Test5:  Create a Mock() object and assign another Mock object to the method name
##### Your test here
def test_function_c():
    mock = Mock()
    mock.sayhi = Mock(return_value="a") 
    assert function_c(mock) == "A"
#####


def function_d(param):
    output = param.name

    return output.upper()

# TODO: Test6:  Create a Mock() object and assign stuff to attribute names:
##### Your test here 
def test_function_d():
    mock = Mock()
    mock.name = "a"
    assert function_d(mock) == "A"
#####


# this function calls a chain of methods on the given object
def my_function(some_object):

    output = some_object.foo().bar.baz().quux()

    return output.upper()


# TODO: Test7:  
##### Your test here 
def test_my_function():
    mock = Mock()
    mock.foo.return_value.bar.baz.return_value.quux.return_value = 'a'
    assert my_function(mock) == "A"

#####


