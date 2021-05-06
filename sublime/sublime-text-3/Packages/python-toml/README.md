# *python-toml* module for Package Control

This is the *[toml](https://github.com/uiri/toml)* module
bundled for usage with [Package Control](http://packagecontrol.io/),
a package manager
for the [Sublime Text](http://sublimetext.com/) text editor.


## How to use *toml* as a dependency

In order to tell Package Control
that you are using the *sublime-toml* module
in your ST package,
create a `dependencies.json` file
in your package root
with the following contents:

```js
{
   "*": {
      ">=3000": [
         "python-toml"
      ]
   }
}
```

If the file exists already,
add `"python-toml"` to the every dependency list.

Then run the **Package Control: Satisfy Dependencies** command
to make Package Control
install the module for you locally
(if you don't have it already).

After all this
you can use `import toml`
in any of your Python plugins.

See also:
[Documentation on Dependencies](https://packagecontrol.io/docs/dependencies)



## License

The contents of the root folder
in this repository
are released
under the *public domain*.
The contents of the `all/` folder
fall under *their own bundled licenses*.

## Links

- [toml](https://github.com/uiri/toml)
- [Package Control](http://packagecontrol.io/)
- [Sublime Text](http://sublimetext.com/)
- [pypi](https://pypi.python.org/pypi/toml)
