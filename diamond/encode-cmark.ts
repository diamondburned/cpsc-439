import { html } from "https://deno.land/x/literal_html@1.1.0/mod.ts";

async function main() {
	let input = await Deno.readTextFile(Deno.args[0]);

	// Replace math blocks.
	input = input.replaceAll(
		/\$\$\s*([\s\S]*?)\s*\$\$/gm,
		(_, math) => {
			math = unescapeHTML(math);
			return html`<p>
				<img
					src="${latexImageURL(math)}"
					data-equation-content="${{ attr: math }}"
				/>
			</p>`;
		},
	);

	// Replace inline math segments.
	input = input.replaceAll(/\$([\s\S]+?)\$/gm, (_, math) => {
		math = unescapeHTML(math);
		return html`<img
			src="${latexImageURL(math)}"
			data-equation-content="${{ attr: math }}"
		/>`;
	});

	const output = await exec(["cmark", "--nobreaks", "--unsafe", "--smart"], input);
	console.log(output);
}

async function exec(cmd: string[], stdin = ""): Promise<string> {
	const proc = Deno.run({
		cmd,
		stdin: "piped",
		stdout: "piped",
		stderr: "inherit",
	});

	const stdinEncoder = new TextEncoder();
	await proc.stdin.write(stdinEncoder.encode(stdin));
	proc.stdin.close();

	const stdoutDecoder = new TextDecoder();
	const output = await proc.output();

	const status = (await proc.status()).code;
	if (status != 0) {
		throw `${cmd[0]} failed with status ${status}`;
	}

	return stdoutDecoder.decode(output);
}

function latexImageURL(latex: string): string {
	// latex = latex
	// 	.replaceAll(/\\$/gm, `\\\\`);
	// .replaceAll(/ ([{}])/g, ` \\$1`)
	// .replaceAll(/^({)/g, `\\$1`)
	// .replaceAll(/(})$/g, `\\$1`);
	// console.debug(latex);
	return "https://pi998nv7pc.execute-api.us-east-1.amazonaws.com/production/svg" +
		`?tex=${encodeURIComponent(latex)}&scale=1`;
}

function unescapeHTML(html: string): string {
	return html
		.replaceAll("&amp;", "&")
		.replaceAll("&lt;", "<")
		.replaceAll("&gt;", ">")
		.replaceAll("&quot;", '"')
		.replaceAll("&#39;", "'")
		.replaceAll("&apos;", "'");
}

await main();
