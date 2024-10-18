from django.shortcuts import render, get_object_or_404, redirect
from .models import SubCat
from cat.models import Cat

# Sub Category List Function For Admin Panel
def subcat_list(request):
    if not request.user.is_authenticated:
        return redirect('mylogin')

    subcat = SubCat.objects.all()
    return render(request, 'back/subcat_list.html', {'subcat': subcat})


# Sub Category Add Function For Admin Panel
def subcat_add(request):
    if not request.user.is_authenticated:
        return redirect('mylogin')

    cat = Cat.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        catid = request.POST.get('cat')

        if name == "":
            error = "All Fields Required"
            return render(request, 'back/error.html', {'error': error})

        if len(SubCat.objects.filter(name=name)) != 0:
            error = "This Name Used Before"
            return render(request, 'back/error.html', {'error': error})

        catname = Cat.objects.get(pk=catid).name
        b = SubCat(name=name, catname=catname, catid=catid)
        b.save()

        return redirect('subcat_list')

    return render(request, 'back/subcat_add.html', {'cat': cat})


# Sub Category Edit Function For Admin Panel
def subcat_edit(request, pk):
    if not request.user.is_authenticated:
        return redirect('mylogin')

    subcat = get_object_or_404(SubCat, pk=pk)
    cat = Cat.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        catid = request.POST.get('cat')

        if name == "":
            error = "All Fields Required"
            return render(request, 'back/error.html', {'error': error})

        catname = Cat.objects.get(pk=catid).name
        subcat.name = name
        subcat.catname = catname
        subcat.catid = catid
        subcat.save()

        return redirect('subcat_list')

    return render(request, 'back/subcat_edit.html', {'subcat': subcat, 'cat': cat})


# Sub Category Delete Function For Admin Panel
def subcat_delete(request, pk):
    if not request.user.is_authenticated:
        return redirect('mylogin')

    subcat = get_object_or_404(SubCat, pk=pk)
    subcat.delete()
    return redirect('subcat_list')
