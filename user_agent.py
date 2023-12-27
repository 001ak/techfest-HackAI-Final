# user.py

from uagents.setup import fund_agent_if_low
from uagents import Agent, Context, Model
import sys

# Address of temperature_alert agent
RECIPIENT_ADDRESS = "agent1qfel6ce4667f2j5f7yr2qzeapeyjc5gx7sakg6dx32ej4rjhr9qskqnnyek"

# setting default values
prefered_min_temp=10.0
prefered_max_temp=30.0
prefered_location="New York"


class ProductRequest(Model):
    product_name: str

class ProductResponse(Model):
    message: str

# class TemperatureRequest(Model):
#     min_temperature: float
#     max_temperature: float
#     location: str

# class TemperatureResponse(Model):
#     message: str



# Taking port for user from command line
# user_port=int(sys.argv[1])
# SEED=f"seed_{user_port}"
# ENDPOINT_URI=f"http://127.0.0.1:{user_port}/submit"

# Creating the user agent
user_agent = Agent(
    name="user_agent",
    port=8001,
    seed="user agent secret phrase",
    endpoint=["http://127.0.0.1:8001/submit"],
)

fund_agent_if_low(user_agent.wallet.address())

# on startup take input for min,max temperature and location from user
@user_agent.on_event("startup")
async def introduce_agent(ctx: Context):
    global product_name_ip
    product_name_ip = str(input("Enter product to search: "))

# user communicates with the temperature_agent in an interval of 20 sec
# If temperature of provided location is out of bounds, user gets an Alert
# @user_agent.on_interval(period=20.0, messages=ProductRequest)
# async def interval(ctx: Context):
#     completed = ctx.storage.get("completed")

#     if not completed:
#         await ctx.send(RECIPIENT_ADDRESS, ProductRequest(product_name=product_name_ip))


final_result=""

def search_for_product(input):
    await ctx.send(RECIPIENT_ADDRESS, ProductRequest(product_name=input))

def return_result(input):
    global final_result
    final_result=input


@user_agent.on_message(model=ProductResponse, replies=ProductRequest)
async def handle_query_response(ctx: Context, sender: str, msg: ProductResponse):
    # ctx.logger.info(f"Received message from {sender}: {msg.message}")
    global final_result
    final_result=msg.message
    # return_result(msg.message)

if __name__ == "__main__":
    user_agent.run()
