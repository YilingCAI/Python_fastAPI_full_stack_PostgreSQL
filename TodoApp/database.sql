CREATE TABLE IF NOT EXISTS public.users(
    id SERIAL,
    email varchar(20) UNIQUE, 
    username varchar(20) UNIQUE, 
    first_name varchar(20), 
    last_name varchar(20), 
    hashed_password varchar(20), 
    is_active boolean default True, 
    role varchar(20),
	PRIMARY KEY(id)
	);


CREATE TABLE IF NOT EXISTS public.todos
(
    id SERIAL,
    title character varying(20) COLLATE pg_catalog."default",
    description character varying(20) COLLATE pg_catalog."default",
    priority integer,
    complete character varying(20) COLLATE pg_catalog."default",
    owner_id integer,
    CONSTRAINT todos_pkey PRIMARY KEY (id),
    CONSTRAINT fk_users FOREIGN KEY (owner_id)
        REFERENCES public.users (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.todos
    OWNER to dbrole;


ALTER TABLE IF EXISTS public.users
    OWNER to dbrole;