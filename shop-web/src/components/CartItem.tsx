import { Minus, Plus, Trash2 } from 'lucide-react';
import { CartItem as CartItemType } from '../services/api';

interface CartItemProps {
  item: CartItemType;
  onUpdateQuantity: (itemId: string, quantity: number) => void;
  onRemove: (itemId: string) => void;
}

export const CartItem = ({ item, onUpdateQuantity, onRemove }: CartItemProps) => {
  const product = item.product;

  if (!product) return null;

  return (
    <div className="flex items-center space-x-4 bg-white p-4 rounded-lg shadow">
      <img
        src={product.image_url}
        alt={product.name}
        className="w-20 h-20 object-cover rounded"
      />
      <div className="flex-1">
        <h3 className="font-semibold text-gray-900">{product.name}</h3>
        <p className="text-sm text-gray-500">{product.category}</p>
        <p className="text-blue-600 font-semibold mt-1">
          ${product.price.toFixed(2)}
        </p>
      </div>
      <div className="flex items-center space-x-2">
        <button
          onClick={() => onUpdateQuantity(item.id, item.quantity - 1)}
          className="p-1 rounded-md hover:bg-gray-100"
        >
          <Minus className="h-4 w-4" />
        </button>
        <span className="w-12 text-center font-semibold">{item.quantity}</span>
        <button
          onClick={() => onUpdateQuantity(item.id, item.quantity + 1)}
          className="p-1 rounded-md hover:bg-gray-100"
        >
          <Plus className="h-4 w-4" />
        </button>
      </div>
      <div className="text-right">
        <p className="font-bold text-gray-900">
          ${(product.price * item.quantity).toFixed(2)}
        </p>
        <button
          onClick={() => onRemove(item.id)}
          className="mt-2 text-red-600 hover:text-red-800 flex items-center space-x-1"
        >
          <Trash2 className="h-4 w-4" />
          <span className="text-sm">Remove</span>
        </button>
      </div>
    </div>
  );
};
