
--Add Item 
BEGIN ; 
INSERT  INTO "Bag"
VALUES (1,1);
--Commit/ roll back  transaction
INSERT  INTO "BagItem"
VALUES (1, 3, 10);
UPDATE "Product"
SET quantity = quantity - 10  
WHERE  id = 3;
COMMIT;