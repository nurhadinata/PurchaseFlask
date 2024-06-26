DROP TABLE IF EXISTS user;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS product_odoo
(
    id integer NOT NULL DEFAULT nextval('product_product_id_seq'::regclass),
    default_code character varying COLLATE pg_catalog."default",
    active boolean,
    product_tmpl_id integer NOT NULL,
    barcode character varying COLLATE pg_catalog."default",
    combination_indices character varying COLLATE pg_catalog."default",
    volume numeric,
    weight numeric,
    can_image_variant_1024_be_zoomed boolean,
    message_main_attachment_id integer,
    create_uid integer,
    create_date timestamp without time zone,
    write_uid integer,
    write_date timestamp without time zone,
    gross_weight numeric,
    pack_uom_id integer,
    is_pallet boolean,
    sub_category character varying COLLATE pg_catalog."default",
    substance character varying COLLATE pg_catalog."default",
    master_code character varying COLLATE pg_catalog."default",
    sub_commodity character varying COLLATE pg_catalog."default",
    commodity character varying COLLATE pg_catalog."default",
    person_in_charge character varying COLLATE pg_catalog."default",
    qty_pallet numeric,
    uom_char character varying COLLATE pg_catalog."default",
    cost_uom character varying COLLATE pg_catalog."default",
    conversion_cost_uom double precision,
    cost_bom_id integer,
    cost_price_currency double precision,
    cost_currency_id integer,
    x_color character varying COLLATE pg_catalog."default",
    cost_bom_id2 integer,
    cost_price_currency2 double precision,
    packaging_set_id integer,
    foh_product_id integer,
    percent_shrinkage double precision,
    cost_bom_id3 integer,
    cost_bom_id4 integer,
    cost_price_currency4 double precision,
    CONSTRAINT product_product_pkey PRIMARY KEY (id),
    CONSTRAINT product_product_barcode_uniq UNIQUE (barcode),
)