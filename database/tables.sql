CREATE TABLE IF NOT EXISTS category(
    id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS nutriscore(
    id BIGINT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nutriscore_letter VARCHAR(1) NOT NULL UNIQUE
);


CREATE TABLE IF NOT EXISTS product(
    id BIGINT UNSIGNED NOT NULL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    nutriscore_id BIGINT UNSIGNED NOT NULL,
    link VARCHAR(255) NOT NULL,

    FOREIGN KEY (nutriscore_id) REFERENCES nutriscore(id)
);

CREATE TABLE IF NOT EXISTS store(
    store_id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    store_name VARCHAR(150) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS product_category(
    product_id BIGINT UNSIGNED,
    category_id INT UNSIGNED,

    PRIMARY KEY (product_id, category_id),
    FOREIGN KEY (product_id) REFERENCES product(id),
    FOREIGN KEY (category_id) REFERENCES category(id)
);


CREATE TABLE IF NOT EXISTS product_store(
    product_id BIGINT UNSIGNED NOT NULL,
    store_id INT UNSIGNED NOT NULL,

    PRIMARY KEY (product_id, store_id),
    FOREIGN KEY (product_id) REFERENCES product(id),
    FOREIGN KEY (store_id) REFERENCES store(store_id)
);

CREATE TABLE IF NOT EXISTS favorite(
    product_original_id BIGINT UNSIGNED,
    product_substitute_id BIGINT UNSIGNED,

    PRIMARY KEY (product_original_id, product_substitute_id),
    FOREIGN KEY (product_original_id) REFERENCES product(id),
    FOREIGN KEY (product_substitute_id) REFERENCES product(id)
)
