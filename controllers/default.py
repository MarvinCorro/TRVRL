# -*- coding: utf-8 -*-
### required - do no delete
def user(): return dict(form=auth())
def download(): return response.download(request,db)
def call(): return service()
### end requires
def index():
    return dict(message="Mapping the world, for travelers")

def error():
    return dict()

@auth.requires_login()
def destinations_manage():
    form = SQLFORM.smartgrid(db.t_destinations,onupdate=auth.archive)
    return locals()

@auth.requires_login()
def profile_manage():
    return dict(bla="testing")

def users():
    """
    Display user profile
    """
    if request.args(0) is not None:
        uid = request.args(0)
        user = db.auth_user[request.args(0)]
        name = user.first_name + ' ' + user.last_name
        context = dict(message=name)
        return response.render('default/index.html', context)
    else:
        # TODO do something sensible?
        return redirect(URL('default','index'))
