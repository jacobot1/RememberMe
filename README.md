# RememberMe

This was my first ever Python app. It's a very simple terminal app for remembering things.

## Setup

Run rm_init.py. This will create 3 JSON files for storing people, places, and things to remember.

## Usage

Run rememberme.py. A prompt will appear.

```
Search or type a command... 
```

Entering a text string will search the JSON files for any relevant people, places, or things.

Prefixing an entry with a "!" signifies a command. To browse your content, type:

```
!browse
```

To create a new entry, type:

```
!new
```

To delete an entry, type:

```
!del
```

To exit the program, type:

```
!exit
```

That's pretty much it. Feel free to fork this and make it better or use it for education.
