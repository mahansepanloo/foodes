from home.models import Food



class Cart:
    def __init__(self,request):
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart']={}
        self.cart = cart


    def __iter__(self):
        key = self.cart.keys()
        food = Food.objects.filter(id__in=key)
        cart=self.cart.copy()
        for item in food:
            cart[str(item.id)]['name']=item

        for item in cart.values():
            item['total_price'] = int(item['price']) * item['num']
            yield item

    def __len__(self):
        return (sum(item['num'] for item in self.cart.values()))

    def Total_price(self):
        return (sum(item['total_price'] for item in self.cart.values()))



    def add(self,food,num):
        food_id = str(food.id)
        if not food_id in self.cart:
            self.cart[food_id] = {
                'num':0,
                'price':str(food.price)
            }
        self.cart[food_id]['num']+=num
        self.session.modified = True

    def remove(self,food):
        food_id = str(food.id)
        if food_id in self.cart:
            del self.cart[food_id]
            self.session.modified =True



    def clear(self):
        del self.session['cart']
        self.session.modified =True





