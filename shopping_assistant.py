# shopping_assistant_agent.py

from uagents.setup import fund_agent_if_low
from uagents import Agent, Context, Model
from products import search,price_comparison

class ProductRequest(Model):
    product_name: str

class ProductResponse(Model):
    message: str

# Creating the temperature agent 
shopping_assistant_agent = Agent(
    name="shopping_assistant_agent",
    port=8000,
    seed="shopping_assistant_agent secret phrase",
    endpoint=["http://127.0.0.1:8000/submit"],
)

fund_agent_if_low(shopping_assistant_agent.wallet.address())

# Function to send alert to the user if current temperature is out of bounds of provided min,max temperature
async def check_product_and_alert(ctx: Context,msg: ProductRequest,sender: str):
    # get the current temperature of the provided location
    searched_product = search(msg.product_name)

    if searched_product:
        get_types=price_comparison(msg.product_name)
        print(get_types)
        await ctx.send(sender, ProductResponse(message=f"Product is available")) 
    else:
        await ctx.send(sender, ProductResponse(message=f"Product is not available")) 

@shopping_assistant_agent.on_message(model=ProductRequest, replies=ProductResponse)
async def handle_query_request(ctx: Context, sender: str, msg: ProductRequest):
    await check_product_and_alert(ctx,msg,sender)

if __name__ == "__main__":
    shopping_assistant_agent.run()



# The below code can be used to get the address of this agent

# @shopping_assistant_agent.on_event("startup")
# async def introduce_agent(ctx: Context):
#     ctx.logger.info(f"Hello, I'm agent {ctx.name} and my address is {ctx.address}.")