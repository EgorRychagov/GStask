# Entity container / request handler
## *Description*
This program was created for custom entitie's data containing. It also allows to get any registered data at one request via special structure.
## Quick launch
Use all the functionals by importing `data_shell.py`. You may also check out usage examples in `test.py`
## Data structures
All the data is contained in Python dictionaries and lists. Here some definitions to understand containing structures:
- `nature` - entitie's nature, *e.g.* player, polygon, server or anything you assume to contain;
- `field` - entitie's property;
- `value_getter` - propertie's meaning, getting as a function's reference
- `id` - specify it if there is plenty of entitie's objects to differ
### Registered data structure
 
 >{\
 >nature&emsp;:&emsp;{\
 >&emsp;&emsp;&emsp;&emsp;id &emsp;:&emsp;{\
 >&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;field&emsp;:&emsp;value_getter\
 >&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; &emsp;}\
 >&emsp;&emsp;&emsp;&emsp;&emsp;}\
 >nature&emsp;:&emsp;{\
 >&emsp;&emsp;&emsp;&emsp;field&emsp;:&emsp;value_getter\
 >&emsp;&emsp;&emsp;&emsp;&emsp;}\
 >}

You may not specify `id` if entity is single object

## Request and response structures

>request&emsp;=&emsp;{\
>&emsp;&emsp;&emsp;&emsp;nature&emsp;:&emsp;{id&emsp;:&emsp;[&emsp;],&emsp;fields&emsp;:&emsp;[&emsp;]}\
>&emsp;&emsp;&emsp;&emsp;nature&emsp;:&emsp;{fields&emsp;:&emsp;[&emsp;]}\
>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;}\
>response&emsp;=&emsp;{\
>&emsp;&emsp;&emsp;&emsp;nature&emsp;:&emsp;{id&emsp;:&emsp;{fields&emsp;:&emsp;value_getters}}\
>&emsp;&emsp;&emsp;&emsp;nature&emsp;:&emsp;{fields&emsp;:&emsp;value_getters}\
>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;}\
Specify `id` and `fields` in lists to request these fields of several objects

## Functionals
- class *InfoStack*
>- `register()` - registrates entitie's properties and automatically updates responses
>- `pull()` - gets a value by field
>- `request_reg()` - registeres a request type by name
>- `request_pull()` - pulls request by name
>- `response_pull()` - pulls response (always up to date) by the name of request 
- class *Parser*
>- `parse()` - provides single time response generation
