from django.shortcuts import render, redirect


mock_data_list = [
    {
        "id": 1,
        "name": "ProductA",
        "content": "상품A 입니다.",
        "price":1000,
    },
    {
        "id": 2,
        "name": "ProductB",
        "content": "상품B 입니다.",
        "price":1500,
    },
    {
       "id": 3,
        "name": "ProductC",
        "content": "상품C 입니다.",
        "price":12000,
    },
    {
        "id": 4,
        "name": "ProductD",
        "content": "상품D 입니다.",
        "price":2000,
    },
    {
        "id": 5,
        "name": "ProductE",
        "content": "상품E 입니다.",
        "price":8000,
    },
    {
        "id": 6,
        "name": "ProductF",
        "content": "상품F 입니다.",
        "price":6000,
    },
    {
        "id": 7,
        "name": "ProductG",
        "content": "상품G 입니다.",
        "price":5000,
    },
    {
        "id": 8,
        "name": "ProductH",
        "content": "상품H 입니다.",
        "price":6000,
    },
    {
        "id": 9,
        "name": "ProductI",
        "content": "상품I 입니다.",
        "price":1000,
    },
    {
        "id": 10,
        "name": "ProductJ",
        "content": "상품J 입니다.",
        "price":60000,
    },
]


def product(request):
    context = {"mock_data_list": mock_data_list}
    return render(request, "product/product.html", context)



def productdetail(request, pk):
    context = {"product": mock_data_list[pk - 1]}
    return render(request, "product/productdetail.html", context)
