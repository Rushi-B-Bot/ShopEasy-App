import { Routes, Route } from 'react-router-dom';
import { Home } from '../pages/Home';
import { ProductDetails } from '../pages/ProductDetails';
import { Login } from '../pages/Login';
import { Register } from '../pages/Register';
import { Cart } from '../pages/Cart';
import { Checkout } from '../pages/Checkout';
import { ProtectedRoute } from './ProtectedRoute';

export const AppRoutes = () => {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/product/:id" element={<ProductDetails />} />
      <Route path="/login" element={<Login />} />
      <Route path="/register" element={<Register />} />
      <Route
        path="/cart"
        element={
          <ProtectedRoute>
            <Cart />
          </ProtectedRoute>
        }
      />
      <Route
        path="/checkout"
        element={
          <ProtectedRoute>
            <Checkout />
          </ProtectedRoute>
        }
      />
    </Routes>
  );
};
