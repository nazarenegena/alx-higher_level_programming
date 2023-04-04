#!/usr/bin/python3
#include <Python.h>

void print_python_string(PyObject *p)
{
Py_ssize_t length;
char *str;

// Checking p  string
if (!PyUnicode_Check(p)) {
printf("Error: PyObject is not a string\n");
return;
}

// Get the string length
length = PyUnicode_GET_LENGTH(p);

// Get encoded UTF-8 string
str = PyUnicode_AsUTF8(p);

// Print string
printf("String value: %s\n", str);

// Print length of string
printf("Length: %zd\n", length);
}

