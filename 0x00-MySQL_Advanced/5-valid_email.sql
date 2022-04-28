-- Write a SQL script that creates a trigger that resets the attribute valid_email only when the email has been changed.

CREATE TRIGGER decreases_the_quantity AFTER INSERT ON orders
    FOR EACH ROW
        UPDATE items SET quantity = quantity - NEW.number
        WHERE items.name = NEW.item_name;
