# HOME WORKS

## 1.CartManager.py

   1.Finishi Class from Cart Manager.
    

    realizat
<!-- ## 2.Details 
  
    | Link to                                               +
    v -->

## 3.view-cart

    HW:
       view-cart                                              +
    * read client_id from cookie 
    * HINT you could also store cart_id in the cookies
    * make a table on this page
<!--        ------------------------------------------------------    +
    |no  | name  | price | quntity| cost |  operations   |    +
    ------------------------------------------------------    +
    | 1. | First | 10.0   | 2     | 20   |   +  X  -     |    +
    ------------------------------------------------------    + -->

## 3.dashboard.py
   
   REALIZAT 

<!-- 
        HW 
        - use the HTML table to show the product stock here 
        - name, q , operations
        - add a link to /web/add-product.py
        - make a from this page which will allow adding new products to stock -->


    # HW: these verification should be on ALL admin pages
    if admin_id is in the cookies

    if cookie_data !='':
        cookie_key, cookie_value = cookie_data.split('=')


    if cookie_key == 'admin_id':
        print(f"Refresh: 0; URL=/web/admin/sign-in.py")


## 4.sign-up.py

    product_id = data.getvalue('id')
    CartManager.addItem(product_id)
    # HW1: finish the addItem() method



