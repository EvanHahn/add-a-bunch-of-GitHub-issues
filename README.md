add a bunch of GitHub issues
============================

I had a file like this:

    fix the bug
    add the feature
    break the other feature
    ...

I wanted to add each line as a GitHub issue. So I built this little thing. To do this:

    # clone this sucker and cd inside
    virtualenv env
    source env/bin/activate
    pip install -r requirements.txt

    # answer its questions
    ./add-a-bunch-of-github-issues.py

It has a ton of `sleep`s so that you don't piss GitHub off.
