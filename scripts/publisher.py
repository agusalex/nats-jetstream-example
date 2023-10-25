import asyncio
import nats


async def main():
    print("Connecting to nats")
    nc = await nats.connect("nats://admintest:admintest@nats:4222")
    js = nc.jetstream()

    await js.add_stream(name="agusalex999", subjects=["agusalex999"])
    i = 0
    while True:
        ack = await js.publish("agusalex999", f'Hello JS! {i}'.encode())
        print(f'Ack: stream={ack.stream}, sequence={ack.seq}')
        i += 1
        await asyncio.sleep(2)


if __name__ == '__main__':
    asyncio.run(main())
