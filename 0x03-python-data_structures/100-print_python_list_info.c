#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <time.h>
#include <Python.h>

/**
 * print_python_list_info - Prints basic information about a Python list.
 * @p: A pointer to the Python list object.
 */
void print_python_list_info(PyObject *p) {
    Py_ssize_t size, alloc, i;
    PyObject *element;

    size = PyList_Size(p);
    alloc = ((PyListObject *)p)->allocated;

    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", alloc);

    for (i = 0; i < size; i++) {
        element = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(element)->tp_name);
    }
}
