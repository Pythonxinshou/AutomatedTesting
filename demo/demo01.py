def test01(*args, **kwargs):
    print(args)
    print(**kwargs)


test01('小', 1, 3, name='da', age=200)
