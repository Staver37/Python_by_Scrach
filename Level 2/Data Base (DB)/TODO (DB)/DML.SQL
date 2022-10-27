-- INSERT INTO - SINGLE VALUE
INSERT INTO    
    public.tasks
       (title, done)
    VALUES
        ('Another Task', false);

-- INSERT INTO - MULTI VALUE
INSERT INTO
    public.tasks
       (title, done)
    VALUES
        ('Another Good Task A', false)
        ('Another Good Task B', true)
        ('Another Good Task C', false)
        ('Another Good Task D', true)
        ('Another Good Task E', false)
        ('Another Good Task F', true)

-- SELECT STANDARD
SELECT title, done
    FROM public.tasks;

-- SELECT  + WHERE
SELECT title, done
    FROM public.tasks
    WHERE done = true;
    

SELECT title, done
    FROM public.tasks
    WHERE title = 'another Good Task D'

SELECT title, done
    FROM public.tasks
    WHERE title   LIKE 'Another%';

SELECT title, done
    FROM public.tasks
    WHERE title   LIKE '%Good%';

-- UPDATE STANDARD
UPDATE public.tasks
	SET done=false
    WHERE title ='Another Good Task D';
	
UPDATE public.tasks
	SET done=false
    WHERE title =true;
	
		
