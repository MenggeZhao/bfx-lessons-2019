## Misc utilities
* Jupyter
* Cookie cutter 
* Ris reference dir 
* Dbhi pipelines
* Github

## Task 1
### Passwordless SSH (10 min)
---

### Instructions
[https://linuxize.com/post/how-to-setup-passwordless-ssh-login/](https://linuxize.com/post/how-to-setup-passwordless-ssh-login/)

### Add bash alias to .bash_profile
```
alias ssr='ssh USER@respublica-an01.research.chop.edu'
alias scv="evansj@refosco.research.chop.edu:"
```
Now in terminal:
```
$ source .bash_profile
```

### Respublica login usage
```
# login to respublica
$ ssr
```

### Copy a file to respublica
```
# copy file to respublica
$ scp some_file.txt $ssr/home/evansj/
```
