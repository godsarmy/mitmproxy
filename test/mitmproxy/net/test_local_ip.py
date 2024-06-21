from mitmproxy.net import local_ip
from ...conftest import skip_no_ipv6


def test_get_local_ip():
    # should never error, but may return None depending on the host OS configuration.
    local_ip.get_local_ip()
    local_ip.get_local_ip("0.0.0.0")
    local_ip.get_local_ip("127.0.0.1")
    local_ip.get_local_ip("invalid!")


@skip_no_ipv6
def test_get_local_ip6():
    # should never error, but may return None depending on the host OS configuration.
    local_ip.get_local_ip6()
    local_ip.get_local_ip6("::")
    local_ip.get_local_ip6("::1")
    local_ip.get_local_ip("invalid!")
