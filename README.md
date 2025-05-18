# Transitioning from OneTick to KX products: A Series of Use Cases

While migrating tick data from OneTick to kdb+, one of the more straightforward aspects is handling raw trade and quote
data. This is because such data can often be re-sourced from market data providers. Therefore, the main focus during
migration lies in rethinking the architecture of the data analytics platform itself.

By shifting from `OneTick Query Language` to the `q` programming language, teams can take full advantage of `kdb+`’s
performance and expressiveness, among other powerful features. This transition also enables seamless integration with
existing Python-based analytics platforms through `PyKX`, resulting in a more flexible and scalable architecture.

In this brief example, I’d like to share a real-world use case that I’ve encountered in my work experience: how to
build an intraday trading volume histogram using `kdb+` along with `Python` technologies.

Assuming you've successfully installed [kdb+](https://code.kx.com/q) and [PyKX](https://code.kx.com/pykx), you can
proceed with building the histogram as follows:

Step 1: Create a CSV file by extracting trade data from a trading API  (`trades_data_retriever.py` script)

Step 2: Upload the CSV file into a kdb+ table and create a Matplotlib histogram using data queried from the kdb+
table (`histogram_creator.py` script)

Potential enhancements for this use case:

- In real-world scenarios, kdb+ tables are partitioned. This allows to achieve an optimal performance when storing /
  retrieving kdb+ data.

- Consider building a kdb+tick architecture when creating a real-time database and historical database with tick data.

**Alpaca Trading API Documentation**

Historical trades (single symbol): [Stock Trades](https://docs.alpaca.markets/reference/stocktradesingle-1)

**KX Documentation**

Database and Programming Language: [kdb+ and q](https://code.kx.com/q)

Python interface library: [PyKX](https://code.kx.com/pykx)

**Environment Setup**

Create Virtual Environment: `python -m venv .venv`

Activate Virtual Environment: `source .venv/bin/activate`

Install Libraries: `pip install requests pykx matplotlib`  