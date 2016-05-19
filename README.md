LINE bot without bot account
----




Update
------


**2016.05.19**

 add *sample.py*.

 *sample.py* allows a LINE user to send a sample message to someone.


**2015.05.28**

`sendImage` and `sendImageWithURL` is fixed.

To send an Image:

    >>> contact = client.contacts[0]
    >>> contact.sendImage('./image.jpg')

Or use:

    >>> contact = client.contacts[0]
    >>> contact.sendImageWithURL('https://avatars3.githubusercontent.com/u/3346407?v=3&s=460')


**2015.03.31**

authToken expiration [issue](https://github.com/carpedm20/LINE/issues/9) solved.

update authToken **automatically**:

    $ pip install line --upgrade

There is nothing to change in your original code.

update authToken **manually**:

    $ pip install line --upgrade
    $ python
    >>> from line import LineClient, LineGroup, LineContact
    >>> client = LineClient("ID", "PASSWORD")
    >>> client.updateAuthToken() # manual update
    True


**2014.08.08**

Some codes are removed because of the request of LINE corporation. You can use library only with `authToken` login.


