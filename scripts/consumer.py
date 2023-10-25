import asyncio
import nats


async def main():
    print("Connecting to nats")
    nc = await nats.connect("nats://admintest:admintest@nats:4222")
    js = nc.jetstream()

    sub = await js.subscribe("agusalex999")

    while True:
        try:
            msg = await asyncio.wait_for(sub.next_msg(), timeout=5.0)
            print(f"Received a message on '{msg.subject}': {msg.data.decode()}")
            await msg.ack()
        except asyncio.TimeoutError:
            print("Timeout while waiting for a message.")


if __name__ == '__main__':
    asyncio.run(main())
