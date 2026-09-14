/*
  # Create E-commerce Schema

  1. New Tables
    - `products`
      - `id` (uuid, primary key)
      - `name` (text)
      - `description` (text)
      - `price` (decimal)
      - `image_url` (text)
      - `category` (text)
      - `stock` (integer)
      - `created_at` (timestamp)
    
    - `cart_items`
      - `id` (uuid, primary key)
      - `user_id` (uuid, references auth.users)
      - `product_id` (uuid, references products)
      - `quantity` (integer)
      - `created_at` (timestamp)
      - `updated_at` (timestamp)
  
  2. Security
    - Enable RLS on both tables
    - Products: Public read access
    - Cart items: Users can only access their own cart items
  
  3. Sample Data
    - Insert sample products for testing
*/

-- Create products table
CREATE TABLE IF NOT EXISTS products (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  name text NOT NULL,
  description text NOT NULL,
  price decimal(10, 2) NOT NULL,
  image_url text NOT NULL,
  category text NOT NULL,
  stock integer NOT NULL DEFAULT 0,
  created_at timestamptz DEFAULT now()
);

-- Create cart_items table
CREATE TABLE IF NOT EXISTS cart_items (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id uuid REFERENCES auth.users(id) ON DELETE CASCADE NOT NULL,
  product_id uuid REFERENCES products(id) ON DELETE CASCADE NOT NULL,
  quantity integer NOT NULL DEFAULT 1,
  created_at timestamptz DEFAULT now(),
  updated_at timestamptz DEFAULT now(),
  UNIQUE(user_id, product_id)
);

-- Enable RLS
ALTER TABLE products ENABLE ROW LEVEL SECURITY;
ALTER TABLE cart_items ENABLE ROW LEVEL SECURITY;

-- Products policies (public read access)
CREATE POLICY "Anyone can view products"
  ON products FOR SELECT
  USING (true);

-- Cart items policies (users can only access their own cart)
CREATE POLICY "Users can view own cart items"
  ON cart_items FOR SELECT
  TO authenticated
  USING (auth.uid() = user_id);

CREATE POLICY "Users can insert own cart items"
  ON cart_items FOR INSERT
  TO authenticated
  WITH CHECK (auth.uid() = user_id);

CREATE POLICY "Users can update own cart items"
  ON cart_items FOR UPDATE
  TO authenticated
  USING (auth.uid() = user_id)
  WITH CHECK (auth.uid() = user_id);

CREATE POLICY "Users can delete own cart items"
  ON cart_items FOR DELETE
  TO authenticated
  USING (auth.uid() = user_id);

-- Insert sample products
INSERT INTO products (name, description, price, image_url, category, stock) VALUES
  ('Wireless Headphones', 'High-quality wireless headphones with noise cancellation', 99.99, 'https://images.pexels.com/photos/3825517/pexels-photo-3825517.jpeg', 'Electronics', 50),
  ('Smart Watch', 'Feature-rich smartwatch with fitness tracking', 199.99, 'https://images.pexels.com/photos/437037/pexels-photo-437037.jpeg', 'Electronics', 30),
  ('Laptop Backpack', 'Durable backpack with laptop compartment', 49.99, 'https://images.pexels.com/photos/2905238/pexels-photo-2905238.jpeg', 'Accessories', 100),
  ('USB-C Cable', 'Fast charging USB-C cable 6ft', 14.99, 'https://images.pexels.com/photos/4526404/pexels-photo-4526404.jpeg', 'Accessories', 200),
  ('Mechanical Keyboard', 'RGB mechanical keyboard with blue switches', 129.99, 'https://images.pexels.com/photos/2115257/pexels-photo-2115257.jpeg', 'Electronics', 40),
  ('Wireless Mouse', 'Ergonomic wireless mouse with precision tracking', 39.99, 'https://images.pexels.com/photos/2115256/pexels-photo-2115256.jpeg', 'Electronics', 75),
  ('Phone Case', 'Protective phone case with shockproof design', 19.99, 'https://images.pexels.com/photos/788946/pexels-photo-788946.jpeg', 'Accessories', 150),
  ('Portable Charger', '20000mAh portable power bank', 34.99, 'https://images.pexels.com/photos/4792285/pexels-photo-4792285.jpeg', 'Electronics', 60)
ON CONFLICT DO NOTHING;