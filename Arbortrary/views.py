from multiprocessing import context
from django.shortcuts import redirect, render
from log_reg_app.models import User
from datetime import datetime
from Arbortrary.models import Tree
from django.contrib import messages


def root(request):
    context = {
        'user': User.objects.get(id=request.session['id']),
        'trees': Tree.objects.all(),
        'page_title': 'Arbortrary',
        'nav_button': 'Plant a tree',
        'nav_button_action': '/trees/new/tree',
    }

    return render(request, 'dashboard.html', context)


def add_new_tree(request):
    context = {
        'user': User.objects.get(id=request.session['id']),
        'form_button': 'Plant',
        'nav_button': 'dashboard',
        'nav_button_action': '/trees',
        'form_action': '/trees/create_tree'
    }
    return render(request, 'add_or_edit_tree.html', context)


def create_tree(request):
    errors = Tree.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/trees/new/tree')
    else:
        species = request.POST['species']
        location = request.POST['location']
        reason = request.POST['reason']
        date_planted = request.POST['date_planted']
        Tree.objects.create(
            species=species, location=location, reason=reason, user=User.objects.get(id=request.session['id']), date_planted=date_planted)
        return redirect('/trees/')


def read_tree_details(request, tree_id):
   
    context = {
        'user': User.objects.get(id=request.session['id']),
        'tree': Tree.objects.get(id=tree_id),
        'nav_button': 'dashboard',
        'nav_button_action': '/trees',

    }
    return render(request, 'tree_details.html', context)


def user_trees(request):
    user = User.objects.get(id=request.session['id'])
    context = {
        'user': user,
        'nav_button': 'dashboard',
        'user_trees': user.trees.all(),
        'nav_button_action': '/trees',
    }
    return render(request, 'user_trees.html', context)


def delete_tree(request, tree_id):
    Tree.objects.get(id=tree_id).delete()
    return redirect('/trees/user/account')


def edit_tree(request, tree_id):
    tree = Tree.objects.get(id=tree_id)
    date_planted = tree.date_planted.strftime('%Y-%m-%d')
    context = {
        'tree': tree,
        'user': User.objects.get(id=request.session['id']),
        'form_button': 'Update',
        'form_action': '/trees/update/' + str(tree_id),
        'date_planted': date_planted,
        'nav_button': 'dashboard',
        'nav_button_action': '/trees',
    }
    return render(request, 'add_or_edit_tree.html', context)


def update_tree(request, tree_id):
    errors = Tree.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/trees/new/tree')
    else:
        tree = Tree.objects.get(id=tree_id)
        tree.species = request.POST['species']
        tree.location = request.POST['location']
        tree.reason = request.POST['reason']
        tree.date_planted = request.POST['date_planted']
        tree.save()
        return redirect('/trees/show/' + str(tree_id))
