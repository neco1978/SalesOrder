--most ordered products
select p.product_code, p.name, sum(d.quantity) total_ordered
from sales_order o, sales_order_details d, product p
where o.order_id = d.order_id
  and d.product_code = p.product_code
group by p.product_code, p.name
order by total_ordered desc;

--most ordered products by year
select p.product_code, p.name, extract('Year' from o.order_date) order_date,sum(d.quantity) total_ordered
from sales_order o, sales_order_details d, product p
where o.order_id = d.order_id
  and d.product_code = p.product_code
group by p.product_code, p.name, extract('Year' from o.order_date)
order by order_date desc, total_ordered desc;

--most ordered branch by year
select c.name, extract('Year' from o.order_date) order_date,sum(d.quantity) total_ordered
from sales_order o, sales_order_details d, customers c
where o.order_id = d.order_id
  and o.customer_id = c.id
group by c.name, extract('Year' from o.order_date)
order by order_date desc, total_ordered desc;

--products has less than 10 items on the stock
select *
from product
where stock_level < 10;


--products hasn't been ordered
select * from product
where product_code not in (select product_code from sales_order_details)
