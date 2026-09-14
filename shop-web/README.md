# E-commerce Frontend Application

A modern, production-ready e-commerce application built with React, TypeScript, Vite, and Supabase.

## Features

- **Product Catalog**: Browse and search products with real-time data from Supabase
- **User Authentication**: Secure email/password authentication with Supabase Auth
- **Shopping Cart**: Add, remove, and update product quantities
- **Protected Routes**: Cart and checkout pages require authentication
- **Responsive Design**: Clean, mobile-friendly UI with Tailwind CSS
- **Real-time Updates**: Cart data synchronized with Supabase database

## Tech Stack

- **Frontend**: React 18 with TypeScript
- **Build Tool**: Vite
- **Routing**: React Router v6
- **Styling**: Tailwind CSS
- **Icons**: Lucide React
- **Backend**: Supabase (Database + Authentication)
- **State Management**: React Context API

## Project Structure

```
src/
├── components/          # Reusable UI components
│   ├── Navbar.tsx
│   ├── Footer.tsx
│   ├── ProductCard.tsx
│   ├── CartItem.tsx
│   └── Loader.tsx
├── pages/              # Page components
│   ├── Home.tsx
│   ├── ProductDetails.tsx
│   ├── Login.tsx
│   ├── Register.tsx
│   ├── Cart.tsx
│   └── Checkout.tsx
├── context/            # React Context providers
│   ├── AuthContext.tsx
│   └── CartContext.tsx
├── services/           # API and service layer
│   ├── supabase.ts
│   └── api.ts
├── routes/             # Routing configuration
│   ├── AppRoutes.tsx
│   └── ProtectedRoute.tsx
└── App.tsx            # Main app component
```

## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   npm install
   ```

3. Environment variables are already configured in `.env`

4. Run the development server:
   ```bash
   npm run dev
   ```

## Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run preview` - Preview production build
- `npm run lint` - Run ESLint
- `npm run typecheck` - Run TypeScript type checking

## Database Schema

### Products Table
- `id` (uuid, primary key)
- `name` (text)
- `description` (text)
- `price` (decimal)
- `image_url` (text)
- `category` (text)
- `stock` (integer)
- `created_at` (timestamp)

### Cart Items Table
- `id` (uuid, primary key)
- `user_id` (uuid, references auth.users)
- `product_id` (uuid, references products)
- `quantity` (integer)
- `created_at` (timestamp)
- `updated_at` (timestamp)

## Security Features

- Row Level Security (RLS) enabled on all tables
- Users can only access their own cart items
- Protected routes for authenticated users only
- Secure authentication with Supabase Auth
- Environment variables for sensitive configuration

## Routes

- `/` - Home page with product listing
- `/product/:id` - Product details page
- `/login` - User login
- `/register` - User registration
- `/cart` - Shopping cart (protected)
- `/checkout` - Checkout page (protected)

## DevOps Ready

- Environment variable configuration via `.env`
- Production build optimization
- TypeScript for type safety
- ESLint for code quality
- Clean architecture for easy deployment

## Usage

1. **Browse Products**: Visit the home page to see all available products
2. **Register/Login**: Create an account or login to access cart features
3. **Add to Cart**: Click on a product and add it to your cart
4. **Manage Cart**: Update quantities or remove items from your cart
5. **Checkout**: Complete your purchase with the checkout form

## Future Enhancements

- Order history tracking
- Product search and filtering
- Product reviews and ratings
- Wishlist functionality
- Payment gateway integration
- Admin dashboard for product management
