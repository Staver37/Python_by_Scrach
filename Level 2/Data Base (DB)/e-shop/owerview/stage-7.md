



## STAGE-7 / Using forms & cookies

- a CGI script hav a very "short memory"
- using cookie system to "restore" memory
- seding data from forms



STANDARD py app running LIFECYCLE

python3 app.py
    v
    v
  id = 1
    v
    v
    v
    v
   end




   client ----->/details.py?id=1
                    v
                    v
                    id = 1
                    v
                    v--->response ----> BROWSER
                    v
                    end

            <add to cart ---> /add-to-cart.py?id=1
                                    v
                                    v
                                    v
                                    v
                                    item = 1 <product 1
                                    v
                                    v
                                   end 

 x---*-*---------------------------------> time                                  
     ^ ^
     ^ ^client -> /add-to-cart?id=1 (card-id=2 > db
     ^
     ^
     client -> /add-to-cart?id=1 (card-id=2 > db









         BACK                       FRONT
    (python app)                   ( HTML)
                        |
                        |
                      cookies
                      sesion
                      url parameters
                 <-------------
                 ------------- -> id
                        |
                        |
                        |




----->/add-to-cart.py?id=1
        if client exist cintinue
        else
          redirect ------------->/sign-up.py
                                    (form)
                                      |
                                 save to DB ---->

<----------------------
redirect
